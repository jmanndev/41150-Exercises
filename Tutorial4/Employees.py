class Employee:
    def __init__(self, empID, name, dob, department, salary):
        self.empID = empID
        self.name = name
        self.dob = dob
        self.department = department
        self.salary = salary

    def Personal_Details(self):
        return self.empID + " " + self.name + " " + self.dob

    def Business_Details(self):
        return self.department + " $" + self.salary

class Programmer(Employee):
    def __init__(self, empID, name, dob, department, salary, specialty, increase_rate):
        super().__init__(self, empID, name, dob, department, salary)
        self.specialty = specialty
        self.increase_rate = increase_rate

    def Personal_Details(self):
        return super().Personal_Details(self)

    def Business_Details(self):
        return super().Business_Details(self) + " " + self.specialty + " " + self.increase_rate

class Administrator(Employee):
    def __init__(self, empID, name, dob, department, salary, grade_level, base_salary):
        super().__init__(self, empID, name, dob, department, salary)
        self.grade_level = grade_level
        self.base_salary = base_salary

    def Personal_Details(self):
        return super().Personal_Details(self)

    def Business_Details(self):
        return super().Business_Details(self) + " " + self.grade_level + " " + self.base_salary
