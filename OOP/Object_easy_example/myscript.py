from user import User

a = User("Arek")
b = User("Viola")
c = User("Piotr")

a.name = "heheh"

print(a.name)
print(b.name)
print(c.name)

print(a.id)
print(b.id)
print(c.id)

print(User.id)