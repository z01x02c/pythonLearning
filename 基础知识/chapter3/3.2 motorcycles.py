motorcycles = ['sfa','afdf','faiufhu']
print(motorcycles)

motorcycles[0] = 'apple'
print(motorcycles)

motorcycles.append('peach')
print(motorcycles)

motorcycles.insert(0,'wine')
print(motorcycles)

del motorcycles[3]
print(motorcycles)

pop_m = motorcycles.pop(2)
print(motorcycles)
print(pop_m)

to_del = 'wine'
motorcycles.remove(to_del)
print(motorcycles)
