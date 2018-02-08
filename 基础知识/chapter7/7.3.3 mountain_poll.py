responses = {}

active = True

while active:
	name = input('\nWhat is your name?\n')
	response = input('Which mountain would you like to climb someday?\n')
	responses[name] = response
	
	repeat = input('Would you like to let another person respond?(yes/no)\n')
	if repeat == 'no':
		active = False

print('----results----\n')
for name, response in responses.items():
	print(name.title() + ' would like to climb ' +  response.title() + '.')
