# (1) Import module from the Python Standard Library

from collections import OrderedDict

## Assign the Instance of OrderedDict to a variable
favorite_languages = OrderedDict()


## Add values to the dictionary
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'


## Loop through the ordered dictionary 

for name, language in favorite_languages.items():
	print(name.title() + '\'s favorite langauge is ' + language.title() + '.')

