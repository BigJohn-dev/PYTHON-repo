from doctor import Doctor
from patient import Patient
from specialization import Specialization
from datetime import date, datetime, timedelta
from specialization import Specialization
from appointment import Appointment

class MedicalRecordSystem():
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, name, dob, phone_number):
        if not self.is_phone_number_valid(phone_number, phone_number):
            raise ValueError("Invalid phone number")
        elif not self.is_valid_dob(dob, dob):
            raise ValueError("Date of birth cannot be in the future")
        else:
            patient = Patient(name, dob, phone_number)
            self.patients.append(patient)
        return self.patients

    def add_doctor(self, name, specialization: Specialization, phone_number):
        if not self.is_phone_number_valid(phone_number, phone_number):
            raise ValueError("Invalid phone number")
        else:
            self.doctors.append(Doctor(name, specialization, phone_number))
        return self.doctors

    @staticmethod
    def is_phone_number_valid(self, phone_number:str):
        if phone_number.startswith(("080", "081", "090", "091", "070")) and len(phone_number) == 11:
            return True
        elif phone_number.startswith("+243") and len(phone_number) == 13:
            return True
        else:
            return False

    @staticmethod
    def is_valid_dob(self, dob: date):
        return dob < datetime.now()

    def schedule_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)

    def search_patient(self, name: str):
        for patient in self.patients:
            if patient.name == name:
                return patient
        return None

    def search_doctor(self, name: str):
        for doctor in self.doctors:
            if doctor.name == name:
                return doctor
        return None


