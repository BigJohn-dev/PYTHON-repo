
class Doctor:
    def __init__(self, name: str, specialization: str, contact_details: str):
        if not name.strip() or not specialization.strip():
            raise ValueError("Name and specialization cannot be empty")
        self.name = name
        self.specialization = specialization
        self.contact_details = contact_details

    def get_doctor_info(self) -> str:
        return f"Dr. {self.name} ({self.specialization}) - Contact: {self.contact_details}"