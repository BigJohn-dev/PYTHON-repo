from MedicalSystemDesign.MSD.class_patient import Patient


class MedicalHistory:
    def __init__(self, patient: Patient, history: str):
        self.patient = patient
        self.history = history

    def set_patient_medical_history(self, history: str):
        self.history = history

    def get_patient_medical_history(self) -> str:
        return self.history

