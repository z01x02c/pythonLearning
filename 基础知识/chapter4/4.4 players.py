# ~ qiepian
players = ['aaa','bbb','ccc','ddd']
print(players[0:3])
print(players[:2])
print(players[-2:])

for player in players[:3]:
	print(player.title())


# ~ copy a list 
# a_foods = foods causes mistakes
foods = ['pizza','apple','cake']
a_foods = foods[:]
