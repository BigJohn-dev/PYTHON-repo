from unittest import TestCase
from class_patient import Patient

class TestPatient(TestCase):
    def setUp(self):
        patient : Patient = Patient("firstname", "lastname", "08045678900", "bigjohn@gmail.com")
        self.patient = patient

    def test_patient_initialization(self):
        self.assertEqual(self.patient.get_first_name(), "firstname")
        self.assertEqual(self.patient.get_last_name(), "lastname")
        self.assertEqual(self.patient.get_contact_details(), "08045678900")
        self.assertEqual(self.patient.get_email(), "bigjohn@gmail.com")

    def test_patient_info_are_not_empty(self):
        self.assertRaises(ValueError, self.patient.set_first_name, " ")
        self.assertRaises(ValueError, self.patient.set_last_name, " ")
        self.assertRaises(ValueError, self.patient.set_contact_details, " ")
        self.assertRaises(ValueError, self.patient.set_email, " ")

    def test_patient_first_name_and_last_name_cannot_contain_digits_or_special_characters(self):
        self.assertRaises(ValueError, self.patient.set_first_name, "f12name")
        self.assertRaises(ValueError, self.patient.set_last_name, "l12name")
        self.assertRaises(ValueError, self.patient.set_first_name, "f_n@me")
        self.assertRaises(ValueError, self.patient.set_last_name, "l_n@me")

    def test_valid_contact(self):
        self.patient.set_contact_details("08012345678")
        self.assertEqual(self.patient._contact_details, "08012345678")

    def test_patient_contact_details_has_eleven_digits(self):
        self.patient.set_contact_details("08045678900")
        self.assertEqual(len(self.patient.get_contact_details()), 11)
        self.assertRaises(ValueError, self.patient.set_contact_details, "080456789")

    def test_invalid_prefix(self):
        self.patient.set_contact_details("08012345678")
        self.assertRaises(ValueError, self.patient.set_contact_details, "02012345678")

    def test_that_contact_details_do_not_contain_alphabets_or_special_characters(self):
        self.patient.set_contact_details("08012345678")
        self.assertRaises(ValueError, self.patient.set_contact_details, "08o1234a678")
        self.assertRaises(ValueError, self.patient.set_contact_details, "080_234@678")

    def test_that_patient_email_is_valid(self):
        self.patient.set_email("bigjohn@gmail.com")
        self.assertRaises(ValueError, self.patient.set_email, "bigjohngmailcom")

    def test_patient_email_cannot_contain_uppercase_letters(self):
        self.assertRaises(ValueError, self.patient.set_email, "BigJohn@gmail.com")

    def test_add_medical_history(self):
        self.patient.add_medical_history("Malaria")

        self.assertEqual(len(self.patient.get_medical_history()), 1)
        self.assertEqual(self.patient.get_medical_history()[0], "Malaria")
