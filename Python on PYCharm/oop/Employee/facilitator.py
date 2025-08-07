from employee import Employee

class Facilitator(Employee):
    def __init__(self, name, age, dob, employee_id, subject):
        super().__init__(name, age, dob, employee_id)
        self.subject = subject

    def __str__(self):
        return f"{super().__str__()}, Subject: {self.subject}"