def show_car(mani,type,**other_info):
	profile = {}
	profile['mani'] = mani
	profile['type'] = type
	for key,value in other_info.items():
		profile[key] = value
	return profile

