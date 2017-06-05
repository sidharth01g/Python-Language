class Employee:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return("Name: " + str(self.name) + "\nID: " + str(self.id))
