from typing import List

from MedicalSystemDesign.MSD.medical_history import MedicalHistory

class Patient:
    def __init__(self, first_name: str, last_name: str, contact_details: str, email: str):
        self._first_name = first_name
        self._last_name = last_name
        self._contact_details = contact_details
        self._email = email
        self.medical_history: List[MedicalHistory] = []

    def set_first_name(self, value: str):
        value = value.strip()
        if value== "":
            raise ValueError("First name cannot be empty")
        if not value.isalpha():
            raise ValueError("First name must contain only letters")
        self._first_name = value

    def get_first_name(self) -> str:
        return self._first_name

    def set_last_name(self, value: str):
        value = value.strip()
        if value == "":
            raise ValueError("Last name cannot be empty")
        if not value.isalpha():
            raise ValueError("Last name must contain only letters")
        self._last_name = value

    def get_last_name(self) -> str:
        return self._last_name

    def set_contact_details(self, value: str):
        if len(value) != 11:
            raise ValueError("Contact details must be 11 digits long")
        if not value.startswith(("080", "081", "090", "091", "070")):
            raise ValueError("Contact details must start with either '080', '081', '090', '091', '070'")
        if not value.isdigit():
            raise ValueError("Contact details must contain only digits")
        self._contact_details = value

    def get_contact_details(self) -> str:
        return self._contact_details

    def set_email(self, value: str):
        if not value.__contains__("@gmail.com"):
            raise ValueError("Email must be a valid Gmail address")
        for char in value:
            if char.isupper():
                raise ValueError("Email cannot contain uppercase letters")
        self._email = value


    def get_email(self) -> str:
        return self._email

    def add_medical_history(self, history: str):
        self.medical_history.append(MedicalHistory(self, history))

    def get_medical_history(self) -> List[MedicalHistory]:
        return self.medical_history

    def get_patient_info(self) -> str:
        return f"Name: {self._first_name} {self._last_name}, Contact: {self._contact_details}, Email: {self._email}"
