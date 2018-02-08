#7-4
# ~ active = True
# ~ while active:
while True:
	ingre = input("\nPlease enter the ingredient you want to add: ")
	if ingre == 'quit':
		# ~ active = False
		break
	else:
		print(ingre.title() + ' has been added.')

