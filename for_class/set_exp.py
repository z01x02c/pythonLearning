"""creat procedure of an expriment"""

active = True
while active:
	trial_num = input('Please enter the number of trials:\n')
	trial_num = int(trial_num)
	if (trial_num % 12 == 0 and trial_num >= 12):
		active = False


for i in range(1,12):
	
