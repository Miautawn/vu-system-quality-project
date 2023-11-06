import uuid
from abc import ABC, abstractproperty, abstractmethod


class Person():
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_full_name(self):
        full_name = self.name + self.surname
        attribute = "Sir. " if self.age > 18 else "Mr. "
        return attribute + full_name


class Administrator(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.username = None
        self.password = None

    def setup_credentials(self, username, password):
        """
        Adds the credentials for the administrator type person
        """
        self.username = username
        self.password = password

    def generate_access_code(self):
        """
        Generate a temporary access code
        """
        return uuid.uuid4()


class Guest(Person):
    def check_in(self, db_client):
        """
        Adds the guest type person
            to the active clients database
        """
        print(f"Adding {self.get_full_name()} to guest list...")
        db_client.insert_guest(self.name, self.surname, self.age)

    def check_out(self, db_client):
        """
        Removes the guest type person from the active
            clients database
        """
        print(f"Removing {self.get_full_name()} from guest list...")
        db_client.remove_guest(self.name, self.surname)


class Room(ABC):
    """
    Abstract Room class, which provides blueprint for various room types
    """

    def __init__(self, number):
        self.number = number

    @abstractproperty
    def beds(self):
        ...

    @abstractproperty
    def chairs(self):
        ...

    @abstractproperty
    def mirrors(self):
        ...

    @abstractproperty
    def base_rate(self):
        ...

    @abstractmethod
    def calculate_cost(self, clients, nights):
        ...


class NormalRoom(Room):

    @property
    def beds(self):
        return 2

    @property
    def chairs(self):
        return 1

    @property
    def mirrors(self):
        return 2

    @property
    def base_rate(self):
        return 50

    def calculate_cost(self, clients, nights):
        return self.base_rate * clients * nights


class PresedentialRoom(Room):

    @property
    def beds(self):
        return 4

    @property
    def chairs(self):
        return 2

    @property
    def mirrors(self):
        return 3

    @property
    def base_rate(self):
        return 100

    def calculate_cost(self, clients, nights):
        return self.base_rate * clients / 2 * nights * 3


class SingleRoom(Room):

    @property
    def beds(self):
        return 1

    @property
    def chairs(self):
        return 0

    @property
    def mirrors(self):
        return 1

    @property
    def base_rate(self):
        return 20

    def calculate_cost(self, clients, nights):
        return self.base_rate * nights
