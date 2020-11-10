class User:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def print_age(self):
        print(self.name, "ma ", self.age, "lat")


User1 = User(21, "Bartek")
User2 = User(20, "Magda")

User1.print_age()
User2.print_age()
