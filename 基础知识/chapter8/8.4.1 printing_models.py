def print_models(un_designs,com_designs):
	while un_designs:
		current_de = un_designs.pop()
		print('Printing model: ' + current_de + '.')
		com_designs.append(current_de)
		
def show_list(com_designs):
	print('\nThe following medels have been printed:')
	for com_design in com_designs:
		print('\t' + com_design)
		
un_designs = ['aa','bb','xc']
com_designs = []

print_models(un_designs[:],com_designs)
show_list(com_designs)
