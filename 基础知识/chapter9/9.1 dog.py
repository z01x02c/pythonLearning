class Dog():
	"""test"""
	def __init__(self,name,age):
		"""formalize name and age"""
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title() + ' is now sitting.')
	def roll_over(self):
		print(self.name.title() + ' is rolled over!')
		
my_dog = Dog('willie',6)
my_dog.sit()
print("My dog's name is " + my_dog.name.title() + ".")
print('My dog is ' + str(my_dog.age) + ' years old.')
