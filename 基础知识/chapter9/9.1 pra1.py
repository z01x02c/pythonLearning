class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		print("Restaurant's name is " + self.restaurant_name.title()+'.')
		print("Cuisine type is " + self.cuisine_type + '.')
		
	def open_restaurant(self):
		print(self.restaurant_name.title() + ' is open now.')
		
	def set_number_served(self,number):
		self.number_served = number
	
	def increment_number_served(self,add_num):
		self.number_served += add_num

restaurant = Restaurant('chinese hot pot','si')
rest2 = Restaurant('sss','dd')

restaurant.describe_restaurant()
restaurant.open_restaurant()

rest2.describe_restaurant()
rest2.open_restaurant()

print(restaurant.restaurant_name.title() + ' has serverd ' + str(restaurant.number_served) + ' customers.')
# ~ restaurant.number_served = 10
restaurant.set_number_served(10)
print(restaurant.restaurant_name.title() + ' has serverd ' + str(restaurant.number_served) + ' customers.')
restaurant.increment_number_served(20)
print(restaurant.restaurant_name.title() + ' has serverd ' + str(restaurant.number_served) + ' customers.')
