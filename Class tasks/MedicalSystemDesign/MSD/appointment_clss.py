import datetime

from MedicalSystemDesign.MSD.class_doctor import Doctor
from MedicalSystemDesign.MSD.class_patient import Patient

class Appointment:
    def __init__(self, patient: Patient, doctor: Doctor, date_time: datetime):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    def schedule_appointment(self):
        print(f"Appointment scheduled for {self.patient.name} with {self.doctor.name} on {self.date_time}")

    def get_appointment_details(self) -> str:
        return f"{self.date_time} - {self.patient.name} with Dr. {self.doctor.name}"

    def cancel_appointment(self) -> str:
        return f"Appointment with Dr. {self.doctor.name} for {self.patient.name} on {self.date_time} canceled."