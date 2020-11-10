class person(object):

	population = 50

	def __init__(self,name,age):
		self.name = name
		self.age = age

	#class method DECORATOR
	#class method is a method where you don't have to have instance of class
	@classmethod
	def getPopulation(cls):
		return cls.population

	#static method
	@staticmethod
	def isAdult(age):
		return age >= 18

	def display(self):
		print(self.name, "is" , self.age, "years old")

newPerson = person('tim', 18)

print(person.getPopulation())