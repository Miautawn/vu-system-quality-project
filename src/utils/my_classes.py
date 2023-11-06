import uuid


class Person:
    def __init__(self, name, surname, age, is_administrator):
        self.name = name
        self.surname = surname
        self.age = age
        self.is_guest = True if is_administrator else False
        self.username = None
        self.password = None

    def get_full_name(self):
        full_name = self.name + self.surname
        attribute = "Sir. " if self.age > 18 else "Mr. "
        return attribute + full_name

    def check_in(self, db_client):
        """
        Adds the guest type person
            to the active clients database
        """
        if self.is_guest:
            print(f"Adding {self.get_full_name()} to guest list...")
            db_client.insert_guest(self.name, self.surname, self.age)
        else:
            print(f"{self.get_full_name()} is not a guest...")

    def check_out(self, db_client):
        """
        Removes the guest type person from the active
            clients database
        """
        if self.is_guest():
            print(f"Removing {self.get_full_name()} from guest list...")
            db_client.remove_guest(self.name, self.surname)
        else:
            print(f"{self.get_full_name()} is not a guest...")

    def setup_credentials(self, username, password):
        """
        Adds the credentials for the administrator type person
        """
        if not self.is_guest:
            self.username = username
            self.password = password
        else:
            print(f"{self.get_full_name()} is not an administrator")

    def generate_access_code(self):
        if not self.is_guest:
            return uuid.uuid4()
        else:
            print(f"{self.get_full_name()} is not an administrator")


class Room:
    def __init__(self, number, room_type):
        self.number = number
        self.room_type = room_type

    @property
    def beds(self):
        if self.room_type == "normal":
            return 2
        elif self.room_type == "presedential":
            return 4
        elif self.room_type == "single":
            return 1

    @property
    def chairs(self):
        if self.room_type == "normal":
            return 1
        elif self.room_type == "presedential":
            return 3
        elif self.room_type == "single":
            return 0

    @property
    def mirrors(self):
        if self.room_type == "normal":
            return 2
        elif self.room_type == "presedential":
            return 4
        elif self.room_type == "single":
            return 2

    def calculate_cost(self, clients, nights):
        if self.room_type == "normal":
            return 50 * clients * nights
        elif self.room_type == "presedential":
            return 100 * clients / 2 * nights * 3
        elif self.room_type == "single":
            return 20 * nights
