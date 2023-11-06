from typing import Any
import os

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from utils.mongodb_utils import HotelMongoDBClient

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
DB_NAME = "fishing_resort_hotel"
ACCOMMODATION_COLLECTION = "accomodations"
GUEST_COLLECTION = "guests"
MAP_REDUCE_COLLECTION = "map_reduce"
ROOMS_COLLECTION = "rooms"


# temporary
class Guest:
    def __init__(self, name):
        self.name = name
        self.guests = []

    def check_in(self, guest_name):
        self.guests.append(guest_name)
        print(f"{guest_name} checked into {self.name}.")

    def check_out(self, guest_name):
        if guest_name in self.guests:
            self.guests.remove(guest_name)
            print(f"{guest_name} checked out of {self.name}.")
        else:
            print(f"{guest_name} is not staying at {self.name}.")

    def list_guests(self):
        print(f"Guests currently staying at {self.name}:")
        for guest in self.guests:
            print(guest)


def get_occupied_rooms(client: Any):
    cursor = client.find(
        collection=GUEST_COLLECTION,
        search_query={},
        projection_query={"keys": {"room_number": 1}},
    )

    occupied_rooms = []
    for doc in cursor:
        for key in doc["keys"]:
            occupied_rooms.append(key["room_number"])

    return occupied_rooms


def get_available_rooms(client: Any):
    occupied_rooms = get_occupied_rooms(client)
    cursor = client.find(
        collection=ACCOMMODATION_COLLECTION,
        search_query={"room_number": {"$exists": True, "$nin": occupied_rooms}},
        projection_query={"room_number": 1},
    )

    return [room["room_number"] for room in cursor]


def get_all_rooms(client: Any):
    cursor = client.find(
        collection=ACCOMMODATION_COLLECTION,
        search_query={"room_number": {"$exists": True}},
        projection_query={"room_number": 1},
    )

    return [room["room_number"] for room in cursor]


def get_all_guests(client: Any):
    cursor = client.find(
        collection=GUEST_COLLECTION, projection_query={"name": 1, "surname": 1}
    )

    return [[guest["name"], guest["surname"]] for guest in cursor]


def view_guest_info(client: Any):
    guests = get_all_guests(client)

    guest_choices = [
        Choice(value=index, name=f"{name[0]} {name[1]}")
        for index, name in enumerate(guests)
    ]
    guest_index = inquirer.select(
        message="Please select a guest:", choices=guest_choices
    ).execute()

    guest_info = list(
        client.find(
            collection=GUEST_COLLECTION,
            search_query={
                "name": guests[guest_index][0],
                "surname": guests[guest_index][1],
            },
        )
    )[0]

    print(f"\nPrinting the info about the guest {guest_info['name']}...")
    print(f"{'name':<20}{guest_info['name']}")
    print(f"{'surname':<20}{guest_info['surname']}")
    print(f"{'phone number':<20}{guest_info['contacts']['phone']}")
    print(f"{'email addresss':<20}{guest_info['contacts']['email']}")
    print(f"{'occupied rooms':<20}{[key['room_number'] for key in guest_info['keys']]}")


def view_room_info(client: Any):
    room_keys = get_all_rooms(client)
    room_key = inquirer.select(
        message="Please select a room:", choices=room_keys
    ).execute()

    room_info = list(
        client.find(
            collection=ACCOMMODATION_COLLECTION, search_query={"room_number": room_key}
        )
    )[0]
    room_type_info = list(
        client.find(
            collection=ACCOMMODATION_COLLECTION,
            search_query={"type_id": room_info["type_id"]},
        )
    )[0]

    print(f"\nPrinting the info about the room {room_key}...")
    print(f"{'room type':<20}{room_type_info['type']}")
    print(f"{'number of beds':<20}{room_type_info['beds']}")
    print(f"{'number of tv':<20}{room_type_info['tv']}")
    print(f"{'has pool':<20}{bool(room_type_info['tv'])}")
    print(f"{'price of the night':<20}{room_info['price']}")


def get_total_booked_room_price_with_aggregate_pipeline(client: Any):
    stage_lookup_rooms = {
        "$lookup": {
            "from": ACCOMMODATION_COLLECTION,
            "localField": "keys.room_number",
            "foreignField": "room_number",
            "as": "joined_rooms",
        }
    }
    stage_unwind_matched_rooms = {"$unwind": "$joined_rooms"}

    stage_group_and_sum = {
        "$group": {"_id": None, "total_booking_price": {"$sum": "$joined_rooms.price"}}
    }
    pipeline = [stage_lookup_rooms, stage_unwind_matched_rooms, stage_group_and_sum]
    result = list(client.aggregate(GUEST_COLLECTION, pipeline))[0][
        "total_booking_price"
    ]
    return float(result)


def main():
    # initialising DB
    hotel_db = HotelMongoDBClient(CONNECTION_STRING, DB_NAME)
    hotel_db.drop_db()

    db_backfill_conf = {
        ACCOMMODATION_COLLECTION: "src/data/accommodations_data.json",
        GUEST_COLLECTION: "src/data/guest_data.json",
    }

    hotel_db.seed_db(db_backfill_conf)

    actions = {
        0: get_occupied_rooms,
        1: get_available_rooms,
        2: get_total_booked_room_price_with_aggregate_pipeline,
        3: get_total_booked_room_price_with_map_reduce,
        4: view_room_info,
        5: view_guest_info
    }

    # main program loop
    print("\nWelcome to the Fishing Resort Hotel management console!")
    while True:
        action = select_action()
        
        if action in actions:
            result = actions[action](hotel_db)
            if result is not None:
                print(result)
        else:
            print("Invalid action selected.")

        proceed = inquirer.confirm(
            message="Would you like to query something else?",
        ).execute()
        if not proceed:
            break
        os.system('clear')

def select_action():
    action_choices = [
        Choice(value=i, name=name) for i, name in enumerate([
            "Get all the currently occupied rooms",
            "Get all the currently available rooms",
            "Get the total price of all occupied rooms (Aggregation Pipeline)",
            "Get the total price of all occupied rooms (MapReduce)",
            "View room info",
            "View guest info",
        ])
    ]
    action = inquirer.select(
        message="Select an action:",
        choices=action_choices
    ).execute()
    return action

if __name__ == "__main__":
    main()
