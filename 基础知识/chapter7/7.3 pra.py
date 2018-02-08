sandwich_orders = ['aaa','bbb','ccc','aaa','aaa']
finished_sandwiches = []

print('Aaa has been used up.')
while 'aaa' in sandwich_orders:
	sandwich_orders.remove('aaa')
	

while sandwich_orders:
	finished_sandwich = sandwich_orders.pop()
	print('I made your ' + finished_sandwich.lower() + ' sandwich.')
	finished_sandwiches.append(finished_sandwich)
	
print(finished_sandwiches)
print(sandwich_orders)
