def init(self, name, id, salary=0.0):
    self.name = name
    self.id = id
    self.salary = salary

def set_salary(self, salary):
    self.salary = salary

def show(self):
    print("Name: %s, ID: %i, Salary: %.2f" % (
        self.name, self.id, self.salary))


attrs = {
    "__init__": init,
    "set_salary": set_salary,
    "show": show
}

superclasses = (object,)  # comma required to make it a tuple
Employee = type('Employee', superclasses, attrs)


emp1 = Employee("Jessica", 1023, 100000)
emp1.show()
emp1.set_salary(120000)
emp1.show()
print(type(emp1))
print(type(Employee))
print(type(type))
