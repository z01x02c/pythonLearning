class Car():
	"""moni cars"""
	def __init__(self,make,model,year):
		"""initialize the attributes"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_description_name(self):
		"""return info"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""print odometer"""
		print("This car has " + str(self.odometer_reading) + " miles on it.")
		
	def update_odometer(self,mileage):
		"""change odometer"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print('You cannot roll back an odometer!')
	
	def increment_odometer(self,miles):
		"""add odometer"""
		self.odometer_reading += miles
		
		
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_description_name())

# ~ my_new_car.odometer_reading = 23
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()
