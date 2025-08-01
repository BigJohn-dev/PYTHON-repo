<<<<<<< HEAD
class SemicolonPayroll:
    def __init__(self):
        self.displayPayroll = []

    def add_employee(self, name, hours_worked, pay_rate):
        if not name.strip():
            return "Enter a valid employee name"
        for employee in self.displayPayroll:
            if employee["name"] == name:
                return "Employee's details already exist"
        gross_pay = hours_worked * pay_rate
        federal_tax = self.federal_withholding(gross_pay)
        state_tax = self.state_withholding(gross_pay)
        net_pay = gross_pay - federal_tax - state_tax
        self.displayPayroll.append({
            "name": name,
            "hours_worked": hours_worked,
            "pay_rate": pay_rate,
            "gross_pay": gross_pay,
            "federal_tax": federal_tax,
            "state_tax": state_tax,
            "net_pay": net_pay
        })
        return "New employee payroll added"

    def view_employee(self):
        if not self.displayPayroll:
            return "<<< No employee details added >>>"
        result = "\nLIST OF SEMICOLON'S EMPLOYEES PAYROLL:\n"
        for i, employee in enumerate(self.displayPayroll, 1):
            result += (f"{i}. Name: {employee['name']}, Hours Worked: {employee['hours_worked']}, "
                      f"Pay Rate: ${employee['pay_rate']:.2f}, Gross Pay: ${employee['gross_pay']:.2f}, "
                      f"Federal Tax (20%): ${employee['federal_tax']:.2f}, State Tax (9%): ${employee['state_tax']:.2f}, "
                      f"Net Pay: ${employee['net_pay']:.2f}\n")
        return result

    def update_payroll(self, index, name, hours_worked, pay_rate):
        if 1 <= index <= len(self.displayPayroll):
            gross_pay = hours_worked * pay_rate
            federal_tax = self.federal_withholding(gross_pay)
            state_tax = self.state_withholding(gross_pay)
            net_pay = gross_pay - federal_tax - state_tax
            self.displayPayroll[index - 1] = {
                "name": name,
                "hours_worked": hours_worked,
                "pay_rate": pay_rate,
                "gross_pay": gross_pay,
                "federal_tax": federal_tax,
                "state_tax": state_tax,
                "net_pay": net_pay
            }
            return f"Employee '{name}' payroll updated"
        return "Invalid employee index"

    def federal_withholding(self, amount):
        if amount < 0:
            return 0.0
        return amount * 0.2

    def state_withholding(self, amount):
        if amount < 0:
            return 0.0
        return amount * 0.09


def main():
    semicolon_payroll = SemicolonPayroll()
    while True:
        print("\nWELCOME TO SEMICOLON AFRICA")
        print("\nSEMICOLON'S PAYROLL PAGE")
        print("...keeping track of your employee's pays")
        payroll_menu = '''
...select an option
=============================
1. Add an Employee payroll
2. View all Employees payroll
3. Update an Employee payroll
4. Exit
=============================
'''
        print(payroll_menu)
        selected = input("Enter your choice (1-4): ")

        if selected == "1":
            print("\nADD AN EMPLOYEE PAYROLL")
            name = input("Enter Employee name: ")
            try:
                hours_worked = float(input("Enter Number of Hours Worked: "))
                if hours_worked < 0 or hours_worked > 168:
                    print("Invalid work hours (must be 0-168)")
                    continue
                pay_rate = float(input("Enter pay rate: "))
                if pay_rate < 0:
                    print("Invalid pay rate")
                    continue
                print(semicolon_payroll.add_employee(name, hours_worked, pay_rate))
            except ValueError:
                print("Invalid input, please enter numeric values for hours and pay rate")

        elif selected == "2":
            print("\nVIEW ALL EMPLOYEES PAYROLL")
            print(semicolon_payroll.view_employee())

        elif selected == "3":
            print("\nUPDATE AN EMPLOYEE PAYROLL")
            try:
                index = int(input("Enter payroll number to edit (1 to {}): ".format(len(semicolon_payroll.displayPayroll))))
                name = input("Enter new Employee name: ")
                hours_worked = float(input("Enter new Number of Hours Worked: "))
                if hours_worked < 0 or hours_worked > 168:
                    print("Invalid work hours (must be 0-168)")
                    continue
                pay_rate = float(input("Enter new pay rate: "))
                if pay_rate < 0:
                    print("Invalid pay rate")
                    continue
                print(semicolon_payroll.update_payroll(index, name, hours_worked, pay_rate))
            except ValueError:
                print("Invalid input, please enter valid numbers")

        elif selected == "4":
            print("...thank you for using our app!")
            print("...@semicolon.africa")
            break
        else:
            print("Instructions are clear, options are from 1 to 4...")


if __name__ == "__main__":
=======
class SemicolonPayroll:
    def __init__(self):
        self.displayPayroll = []

    def add_employee(self, name, hours_worked, pay_rate):
        if not name.strip():
            return "Enter a valid employee name"
        for employee in self.displayPayroll:
            if employee["name"] == name:
                return "Employee's details already exist"
        gross_pay = hours_worked * pay_rate
        federal_tax = self.federal_withholding(gross_pay)
        state_tax = self.state_withholding(gross_pay)
        net_pay = gross_pay - federal_tax - state_tax
        self.displayPayroll.append({
            "name": name,
            "hours_worked": hours_worked,
            "pay_rate": pay_rate,
            "gross_pay": gross_pay,
            "federal_tax": federal_tax,
            "state_tax": state_tax,
            "net_pay": net_pay
        })
        return "New employee payroll added"

    def view_employee(self):
        if not self.displayPayroll:
            return "<<< No employee details added >>>"
        result = "\nLIST OF SEMICOLON'S EMPLOYEES PAYROLL:\n"
        for i, employee in enumerate(self.displayPayroll, 1):
            result += (f"{i}. Name: {employee['name']}, Hours Worked: {employee['hours_worked']}, "
                      f"Pay Rate: ${employee['pay_rate']:.2f}, Gross Pay: ${employee['gross_pay']:.2f}, "
                      f"Federal Tax (20%): ${employee['federal_tax']:.2f}, State Tax (9%): ${employee['state_tax']:.2f}, "
                      f"Net Pay: ${employee['net_pay']:.2f}\n")
        return result

    def update_payroll(self, index, name, hours_worked, pay_rate):
        if 1 <= index <= len(self.displayPayroll):
            gross_pay = hours_worked * pay_rate
            federal_tax = self.federal_withholding(gross_pay)
            state_tax = self.state_withholding(gross_pay)
            net_pay = gross_pay - federal_tax - state_tax
            self.displayPayroll[index - 1] = {
                "name": name,
                "hours_worked": hours_worked,
                "pay_rate": pay_rate,
                "gross_pay": gross_pay,
                "federal_tax": federal_tax,
                "state_tax": state_tax,
                "net_pay": net_pay
            }
            return f"Employee '{name}' payroll updated"
        return "Invalid employee index"

    def federal_withholding(self, amount):
        if amount < 0:
            return 0.0
        return amount * 0.2

    def state_withholding(self, amount):
        if amount < 0:
            return 0.0
        return amount * 0.09


def main():
    semicolon_payroll = SemicolonPayroll()
    while True:
        print("\nWELCOME TO SEMICOLON AFRICA")
        print("\nSEMICOLON'S PAYROLL PAGE")
        print("...keeping track of your employee's pays")
        payroll_menu = '''
...select an option
=============================
1. Add an Employee payroll
2. View all Employees payroll
3. Update an Employee payroll
4. Exit
=============================
'''
        print(payroll_menu)
        selected = input("Enter your choice (1-4): ")

        if selected == "1":
            print("\nADD AN EMPLOYEE PAYROLL")
            name = input("Enter Employee name: ")
            try:
                hours_worked = float(input("Enter Number of Hours Worked: "))
                if hours_worked < 0 or hours_worked > 168:
                    print("Invalid work hours (must be 0-168)")
                    continue
                pay_rate = float(input("Enter pay rate: "))
                if pay_rate < 0:
                    print("Invalid pay rate")
                    continue
                print(semicolon_payroll.add_employee(name, hours_worked, pay_rate))
            except ValueError:
                print("Invalid input, please enter numeric values for hours and pay rate")

        elif selected == "2":
            print("\nVIEW ALL EMPLOYEES PAYROLL")
            print(semicolon_payroll.view_employee())

        elif selected == "3":
            print("\nUPDATE AN EMPLOYEE PAYROLL")
            try:
                index = int(input("Enter payroll number to edit (1 to {}): ".format(len(semicolon_payroll.displayPayroll))))
                name = input("Enter new Employee name: ")
                hours_worked = float(input("Enter new Number of Hours Worked: "))
                if hours_worked < 0 or hours_worked > 168:
                    print("Invalid work hours (must be 0-168)")
                    continue
                pay_rate = float(input("Enter new pay rate: "))
                if pay_rate < 0:
                    print("Invalid pay rate")
                    continue
                print(semicolon_payroll.update_payroll(index, name, hours_worked, pay_rate))
            except ValueError:
                print("Invalid input, please enter valid numbers")

        elif selected == "4":
            print("...thank you for using our app!")
            print("...@semicolon.africa")
            break
        else:
            print("Instructions are clear, options are from 1 to 4...")


if __name__ == "__main__":
>>>>>>> origin/main
    main()