class User():
	def __init__(self,first,last):
		self.first = first
		self.last = last
		self.login_attempts = 0

	def describe(self):
		print("Name: " + self.first.title() + ' ' + self.last.title())
	
	def greet(self):
		print('Hello, ' + self.first.title() + ' ' + self.last.title() + '!')
		
	def increment_login_attempts(self):
		self.login_attempts += 1
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		print('Resetting login attempts...')

user1 = User('aaa','bbb')
user1.describe()
user1.greet()
print('Login attempts: ' + str(user1.login_attempts))
user1.increment_login_attempts()
print('Login attempts: ' + str(user1.login_attempts))
user1.increment_login_attempts()
print('Login attempts: ' + str(user1.login_attempts))
user1.reset_login_attempts()
print('Login attempts: ' + str(user1.login_attempts))
