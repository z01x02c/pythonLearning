pics = ['aaa','bbb','ccc','ddd','eee']

print('The first three items in the list are:')
print(pics[:3])

print('Three items from the middle of the list are')
print(pics[1:4])

print('The last three items in the list are')
print(pics[-3:])

pics_copy = pics[:]
pics.append('fff')
pics_copy.append('ttt')
print('Pics are:')
for pic in pics:
	print(pic)

print('\nPics_copy are:')
for pic_copy in pics_copy:
	print(pic_copy)
