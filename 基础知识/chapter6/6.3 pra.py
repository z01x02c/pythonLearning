rivers = {
	'nile':'egypt',
	'yangtze':'china',
	'aa':'tz',
	}

for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title() + '.')

for river in rivers.keys():
	print(river.title())
	
print('\n')
for river in rivers.values():
	print(river.title())
