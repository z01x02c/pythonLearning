num = input('Enter a integer please:\n')
num = float(num)

if num%2 == 1:
	print(str(int(num)) + ' is odd.')
elif num%2 == 0:
	print(str(int(num)) + ' is even.')
else:
	print('Please enter an INTEGER!')
