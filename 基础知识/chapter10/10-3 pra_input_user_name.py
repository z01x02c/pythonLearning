name = input('Please enter your name:\n')

file_name = 'guest.txt'

with open(file_name,'a') as file_object:
	file_object.write(name.title() + '\n')
	print(name.title() + " has been added to guest list.")
