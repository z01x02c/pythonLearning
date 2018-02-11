def show_sandwichs(*ingredients):
	for ingredient in ingredients:
		print(ingredient.capitalize() + ' is added.')

show_sandwichs('aaa','bb','cc')

def show_car(mani,type,**other_info):
	profile = {}
	profile['mani'] = mani
	profile['type'] = type
	for key,value in other_info.items():
		profile[key] = value
	return profile
	
car = show_car('subaru','outback',
	color = 'blue',
	tow_package = 'True')
print(car)
