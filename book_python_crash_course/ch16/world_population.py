# (1) Create program to print world population data
## Import supporting modules
import json
import pygal
from pygal.style import RotateStyle
from country_codes import get_country_code


## Identify path to json file
filename = 'population_data.json'


## Open File and load json 
with open(filename) as f:
	pop_data = json.load(f)


## Build a dictionary of population data

cc_populations = {}

## Loop over file content and read only data from 2010
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		# print(country_name + ': ' + str(population))
		code = get_country_code(country_name)
		if code:
			# print(code + ': ' + str(population))
			cc_populations[code] = population
		# else:
		# 	print('Error - ' + country_name)


## Grouping Countries by Population, 3 levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop


## Identify how many countries are at each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))


## Add Style to the World Map
wm_style = RotateStyle('#336699')


## Generate World Map
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

## Save file to svg format
wm.render_to_file('world_groups_population.svg') 