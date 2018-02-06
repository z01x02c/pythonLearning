users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
		},
		
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		}
	}
for username, user_info in users.items():
	print('username: ' + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']
	
	print('full name: ' + full_name.title())
	print('location: ' + location.title() + '\n')
