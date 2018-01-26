names = ['sky','cloud','tree']
print(names)

print(names[1])
names[1]='grass'
print(names)

names.insert(0,'giant')
names.insert(2,'sad')
names.append('fairy')
print(names)

print("Sorry for canceling the party.")
pop1 = 'grass'
names.remove(pop1)
print(pop1.title() + ",I am so sorry.")
pop2 = names.pop(1)
print(pop2.title() + ",I am so sorry.")
pop3 = names.pop(1)
print(pop3.title() + ",I am so sorry.")
pop4 = names.pop(1)
print(pop4.title() + ",I am so sorry.")
print(names[0] + ",welcome.")
print(names[1] + ",welcome.")

del names[0]
del names[0]
print(names)
