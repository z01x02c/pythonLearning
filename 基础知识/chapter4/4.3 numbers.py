for value in range(1,5):
	print(value)

print("\n")

numbers = list(range(1,6))
print(numbers)
print("\n")

squares = []
for value in range(1,11):
	# ~ square = value**2
	# ~ squares.append(square)
	squares.append(value**2)
print(squares)

nums = [value**2 for value in range(1,8)]
print(nums)
