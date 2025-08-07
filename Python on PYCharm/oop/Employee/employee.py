from human import Human

class Employee(Human):
    def __init__(self, name, age, dob, employee_id):
        super().__init__(name, age, dob)
        self.employee_id = employee_id

    def __str__(self):
        return f"{super().__str__()}, Employee ID: {self.employee_id}"