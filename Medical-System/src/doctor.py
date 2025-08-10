from specialization import Specialization

class Doctor:
    def __init__(self, name, specialization: Specialization, phone_number):
        self.name = name
        self.specialization = specialization
        self.phone_number = phone_number