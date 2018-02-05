customers = ['aaa','bbb','ccc','ddd','admin']
# ~ customers = []

if customers:
	for customer in customers:
		if customer == 'admin':
			print('Hello Eric, thank you for logging in again.')
		else:
			print('Hello '+str(customer.title())+', thank you for logging in again.')
else:
	print('We need to find some users!')

