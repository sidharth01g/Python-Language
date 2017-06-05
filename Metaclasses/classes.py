class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def set_salary(self, salary):
        self.salart = salary

    def show(self):
        print("Name: %s, ID: %s, Salary: %.1f" % (
            self.name, self.id, self.salary))
