fav_lang = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
	}

for key, people in fav_lang.items():
	print(key.title() + "'s favourite language is " + people + '.')
	
for name in sorted(fav_lang.keys()):
	print(name.title())

for language in set(fav_lang.values()):
	print(language.title())
