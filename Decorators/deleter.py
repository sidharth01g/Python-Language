class Employee(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email_id(self):
        return (
            self.first_name.lower() + '.' + self.last_name.lower() +
            "@acme.com"
        )

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, name):
        first_name, last_name = name.split()
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        self.first_name = None
        self.last_name = None
        print("Deleted name!")


def main():
    employee_1 = Employee("John", "Cena")
    print(employee_1.email_id)
    print(employee_1.full_name)

    print("")
    employee_1.full_name = "Abe Lincoln"
    print(employee_1.email_id)
    print(employee_1.full_name)

    del employee_1.full_name
    print(employee_1.first_name)
    print(employee_1.last_name)


if __name__ == "__main__":
    main()
