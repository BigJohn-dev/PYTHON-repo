from unittest import TestCase
from MedicalSystemDesign.MSD.class_patient import Patient

class TestPatient(TestCase):
    def setUp(self):
        patient : Patient = Patient("f_name", "l_name", "08045678900", "bigjohn@gmail.com")
        self.patient = patient

    def test_patient_initialization(self):
        self.assertEqual(self.patient.get_first_name(), "f_name")
        self.assertEqual(self.patient.get_last_name(), "l_name")
        self.assertEqual(self.patient.get_contact_details(), "08045678900")
        self.assertEqual(self.patient.get_email(), "bigjohn@gmail.com")

    def test_patient_info_are_not_empty(self):
        self.assertRaises(ValueError, self.patient.set_first_name, " ")
        self.assertRaises(ValueError, self.patient.set_last_name, " ")
        self.assertRaises(ValueError, self.patient.set_contact_details, " ")
        self.assertRaises(ValueError, self.patient.set_email, " ")

    def test_patient_contact_details_has_eleven_digits(self):
        self.patient.set_contact_details("08045678900")
        self.assertEqual(len(self.patient.get_contact_details()), 11)
        self.assertRaises(ValueError, self.patient.set_contact_details, "080456789")

    def test_that_patient_email_is_valid(self):
        self.patient.set_email("bigjohn@gmail.com")
        self.assertRaises(ValueError, self.patient.set_email, "bigjohngmailcom")