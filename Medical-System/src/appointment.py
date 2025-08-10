from doctor import Doctor
from patient import Patient
from datetime import date


class Appointment:
    def __init__(self, dates: date, time: str, patient: Patient, doctor: Doctor):
        self.date = dates
        self.time = time
        self.patient = patient
        self.doctor = doctor

    def get_appointment_details(self):
        return f"Appointment on{self.date} {self.time} \nPatient Name:{self.patient} Doctor Name: {self.doctor}"
