from die import Die
import pygal
import numpy as np

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."

hist.x_labels = []
for i in range(2,17):
	i_str = str(i)
	hist.x_labels.append(i_str)

# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('different_dice.svg')

print(frequencies)
# print(results)

