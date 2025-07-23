
class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self._first_name = _first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._email = email

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, f_name):
        if f_name == " ":
            raise ValueError("First name cannot be empty")
        self._first_name = f_name

    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, l_name):
        self._last_name = l_name

    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, phone):
        self._phone_number = phone

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, gmail):
        self._email = gmail
