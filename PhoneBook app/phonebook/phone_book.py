
class PhoneBook:

    def __init__(self, first_name: str, last_name: str, phone_number: str, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def get_first_name(self, f_name) -> str:
        if f_name.strip() == "":
            raise ValueError("First name cannot be empty")
        return self.first_name

    def get_last_name(self, l_name) -> str:
        if l_name.strip() == "":
            raise ValueError("Last name cannot be empty")
        return self.last_name

    def get_phone_number(self, phone_number) -> str:
        if phone_number.strip() == "":
            raise ValueError("Phone number cannot be empty")
        return self.phone_number

    def get_email(self, email) -> str:
        if email.strip() == "":
            raise ValueError("Email cannot be empty")
        return self.email