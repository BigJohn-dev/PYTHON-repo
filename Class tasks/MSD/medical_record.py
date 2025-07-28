from typing import List

from MedicalSystemDesign.MSD.appointment_clss import Appointment
from MedicalSystemDesign.MSD.class_doctor import Doctor
from MedicalSystemDesign.MSD.class_patient import Patient


class MedicalRecord:
    def __init__(self):
        self.patients: List[Patient] = []
        self.doctors: List[Doctor] = []
        self.appointments: List[Appointment] = []

    def add_patient(self, patient: Patient):
        self.patients.append(patient)

    def add_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)

    def schedule_appointment(self, appointment: Appointment):
        self.appointments.append(appointment)
        appointment.schedule_appointment()

    def search_patient(self):
        for patient in self.patients:
            print(patient.get_patient_info())

    def search_doctor(self):
        for doctor in self.doctors:
            print(doctor.get_doctor_info())