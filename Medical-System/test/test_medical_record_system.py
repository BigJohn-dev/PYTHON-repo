import unittest
from datetime import datetime
from medical_reord_system import MedicalRecordSystem
from specialization import Specialization
from appointment import Appointment
from patient import Patient

class TestMedicalRecordSystem(unittest.TestCase):
    def setUp(self):
        self.system = MedicalRecordSystem()
        self.patient = ("James Evans", datetime(2002, 10, 17), "09069672905")
        self.doctor = ("Samson Dave", Specialization.GeneralPractitioner, "08068672405")

    def test_add_patient(self):
        self.system.add_patient("James Evans", datetime(2002, 5, 8), "09069672905")
        self.assertIn("James Evans", self.patient)

    def test_add_doctor(self):
        self.system.add_doctor("Samson Dave", Specialization.GeneralPractitioner, "08068672405")
        self.assertIn("Samson Dave", self.doctor)

    def test_system_cannot_add_patient_when_number_is_invalid(self):
        with self.assertRaises(ValueError):
            self.system.add_patient("James Evans", datetime(2002, 5, 8), "12334556")

    def test_system_cannot_add_doctor_when_number_is_invalid(self):
        with self.assertRaises(ValueError):
            self.system.add_doctor("Samson Dave", Specialization.GeneralPractitioner, "12334556")

    def test_system_cannot_add_patient_when_dob_is_invalid(self):
        with self.assertRaises(ValueError):
            self.system.add_patient("James Evans", datetime(2052, 5, 8), "09069672905")

    def test_system_cannot_add_doctor_when_phone_number_is_invalid(self):
        with self.assertRaises(ValueError):
            self.system.add_doctor("Samson Dave", Specialization.GeneralPractitioner, "12334556")

    def test_schedule_appointment(self   ):
        appointment = Appointment(datetime (2025, 7, 22), "10:00", self.patient, self.doctor)
        self.system.schedule_appointment(appointment)

    def test_search_patient(self):
        self.system.add_patient("James Evans", datetime(2002, 5, 8), "09069672905")
        find_patient = self.system.search_patient("James Evans")
        self.assertEqual(find_patient.name, "James Evans")

    def test_search_doctor(self):
        self.system.add_doctor("Samson Dave", Specialization.GeneralPractitioner, "08068672405")
        find_doctor = self.system.search_doctor("Samson Dave")
        self.assertEqual(find_doctor.name, "Samson Dave")

