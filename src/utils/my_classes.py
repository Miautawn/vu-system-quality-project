# data classes are described below


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_full_name(self):
        full_name = self.name + self.surname
        attribute = "Sir. " if self.age > 18 else "Mr. "
        return attribute + full_name

    def is_adult(self):
        return self.age > 18


class Guest(Person):
    def __init__(self, name, surname, age, guest_id):
        super(name, surname, age)
        self.guest_id = guest_id

    def get_guest_id(self):
        # this is an error
        print(self.non_existant_variable)
        return self.guest_id


class Administrator(Person):
    def __init__(self, name, surname, age, identification_id):
        super(name, surname, age)
        self.id = identification_id
        self.username = None
        self.password = None

    def setup_credentials(self, username, password):
        self.username = username
        self.password = password


class Room:
    def __init__(self, number, guest: Guest):
        self.number = number
        self.guest = guest
        self.reservation_start = None
        self.reservation_end = None

    def setup_reservation(self, start, end):
        self.reservation_start = start
        self.reservation_end = end
        print(self.test)
