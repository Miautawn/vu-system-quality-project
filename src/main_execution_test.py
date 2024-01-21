from typing import Any
import os
import json
import copy
import time

from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from utils.mongodb_utils import HotelMongoDBClient

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"
DB_NAME = "fishing_resort_hotel"
ACCOMMODATION_COLLECTION = "accomodations"
GUEST_COLLECTION = "guests"
MAP_REDUCE_COLLECTION = "map_reduce"
ROOMS_COLLECTION = "rooms"

def generate_seed_data(n, prefix):
    rooms_file = open(f"src/data/rooms_{prefix}.json", "w")
    guest_file = open(f"src/data/guests_{prefix}.json", "w")

    room_template = {
            "room_number": 111,
            "type_id": 1,
            "price": 200
    }

    guest_template = {
        "name": "some_name_2",
        "surname": "some_surname_2",
        "contacts": {
            "phone": "+3701111111",
            "email": "name2.surname2@gmail.com"
        },
        "keys": [
            {
                "room_number": 333
            }
        ]
    }

    rooms = []
    guests = []

    for i in range(n):
        room = copy.deepcopy(room_template)
        room["room_number"] = i

        guest = copy.deepcopy(guest_template)
        guest["keys"][0]["room_number"] = i

        rooms.append(room)
        guests.append(guest)

    json.dump({"rooms": rooms}, rooms_file)
    json.dump({"guests": guests}, guest_file)

def timeit(func, args, n):
    start_time = time.perf_counter()

    for _ in range(n):
        func(*args)

    end_time = time.perf_counter()

    # avg time in miliseconds
    average_time = (end_time - start_time) / n * 1000
    return average_time

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

def get_total_booked_room_price(client: Any):
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
   
    # 10 samples
    generate_seed_data(10, "10")
    db_10 = {
        ACCOMMODATION_COLLECTION: "src/data/rooms_10.json",
        GUEST_COLLECTION: "src/data/guests_10.json",
    }
    hotel_db.drop_db()
    hotel_db.seed_db(db_10)
    print(f"Running with 10 samples...")
    avg_time = timeit(get_occupied_rooms, [hotel_db], 1000)
    print(f"`get_occupied_rooms()` average execution time: {avg_time} ms")
    avg_time = timeit(get_total_booked_room_price, [hotel_db], 1000)
    print(f"`get_total_booked_room_price()` average execution time: {avg_time} ms")
    print("")
    
    # 100 samples
    generate_seed_data(100, "100")
    db_100 = {
        ACCOMMODATION_COLLECTION: "src/data/rooms_10.json",
        GUEST_COLLECTION: "src/data/guests_10.json",
    }
    hotel_db.drop_db()
    hotel_db.seed_db(db_100)
    print(f"Running with 100 samples...")
    avg_time = timeit(get_occupied_rooms, [hotel_db], 1000)
    print(f"`get_occupied_rooms()` average execution time: {avg_time} ms")
    avg_time = timeit(get_total_booked_room_price, [hotel_db], 1000)
    print(f"`get_total_booked_room_price()` average execution time: {avg_time} ms")
    print("")

    # 1000 samples
    generate_seed_data(1000, "1000")
    db_1000 = {
        ACCOMMODATION_COLLECTION: "src/data/rooms_10.json",
        GUEST_COLLECTION: "src/data/guests_10.json",
    }
    hotel_db.drop_db()
    hotel_db.seed_db(db_1000)
    print(f"Running with 1000 samples...")
    avg_time = timeit(get_occupied_rooms, [hotel_db], 1000)
    print(f"`get_occupied_rooms()` average execution time: {avg_time} ms")
    avg_time = timeit(get_total_booked_room_price, [hotel_db], 1000)
    print(f"`get_total_booked_room_price()` average execution time: {avg_time} ms")


if __name__ == "__main__":
    main()
