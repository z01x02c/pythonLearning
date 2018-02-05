cars = ['audi','Bmw','subaru','toyota']

for car in cars:
    if car.lower == 'bmw':
        print(car.upper())
    else:
        print(car.title())
            
print('audi' in cars and 'bmw' in cars)
