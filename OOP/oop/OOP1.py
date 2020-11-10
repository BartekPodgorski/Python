class Dog:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tim", 13)
print(d.get_name())
d2 = Dog("Bill", 15)
d2.set_age(30)
print(d2.get_age())
