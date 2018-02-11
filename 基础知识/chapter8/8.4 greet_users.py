def greet_users(names):
	"""greet each users in the list"""
	for name in names:
		msg = "Hello, " + name.title() + '!'
		print(msg)
		
user_names = ['aa','bb','cc']
greet_users(user_names)
