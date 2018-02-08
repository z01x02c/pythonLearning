un_users = ['alice','brain','candace']
con_users = []

while un_users:
	current_user = un_users.pop()
	print('Verifying user: ' + current_user.title())
	con_users.append(current_user)

print('\nThe following users have  been confirmed:')
for con_user in con_users:
	print(con_user.title())	

con_users.append('brain')
print(con_users)

while 'brain' in con_users:
	con_users.remove('brain')
print(con_users)
