from random import randint

class Die():
	def __init__(self,sides=6):
		self.sides = sides
	
	def roll_die(self):
		print(randint(1,self.sides))
		
roll_1 = Die()
roll_2 = Die(10)
roll_3 = Die(20)
for i in range(10):
	roll_1.roll_die()
for i in range(10):
	roll_2.roll_die()
for i in range(10):
	roll_3.roll_die()

	
