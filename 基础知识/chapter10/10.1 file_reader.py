with open('pi_digits.txt') as file_object:
	'''contents = file_object.read()
	print(contents.rstrip())'''
	
	'''for line in file_object:
		print(line.rstrip())'''
		
	lines = file_object.readlines()
	print(lines)

pi_string = ''
for line in lines:
	pi_string += line.strip()
	
print(pi_string[:12])
print(len(pi_string))
