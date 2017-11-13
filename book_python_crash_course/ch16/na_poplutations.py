# (1) Generate World Map with poplutations
## Import necessary modules
import pygal

## Create install of world map and add unique attributes
wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America' , {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

## Save the file to svg format
wm.render_to_file('na_populations.svg')

