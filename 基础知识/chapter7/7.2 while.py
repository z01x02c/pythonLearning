# ~ current_num = 1
# ~ while current_num <= 5:
	# ~ print(current_num)
	# ~ current_num += 1

prompt = '\nTell me something and I will repeat it back to you.\n'
prompt += 'Enter "quit" to end the program.\n'

active = True
while active:
	message = input(prompt)
	
	if message == 'quit':
		active = False
	else:
		print(message)
