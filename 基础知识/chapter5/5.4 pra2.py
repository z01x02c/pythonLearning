#check users
current_users = ['Aa','bb','cc','dd','ff']
new_users = ['AA','ac','dD','gg','ee']

def all_lower(L1):
	return[s.lower() for s in L1]
	
for new_user in new_users:
	if new_user.lower() in all_lower(current_users):
		print(new_user + ' existed.')
	else:
		print(new_user+' is available.')


nums = range(1,10)
for num in nums:
	if num == 1:
		print('1st')
	elif num == 2:
		print('2nd')
	elif num == 3:
		print('3rd')
	else:
		print(str(num)+'th')
