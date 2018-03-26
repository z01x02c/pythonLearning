def addition():
	num1 = input('Please enter the numbers you want to add:\n')
	num2 = input()

	try:
		sum = float(num1) + float(num2)
	except TypeError and ValueError:
		print('Please enter numbers, not the string.\n')
		addition()
	else:
		print(str(num1) + "+" + str(num2) + "=" + str(sum))

addition()
