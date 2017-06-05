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


def main():
    employee_1 = Employee("John", "Cena")
    print(employee_1.email_id)
    employee_1.last_name = "Bane"
    print(employee_1.email_id)


if __name__ == "__main__":
    main()
