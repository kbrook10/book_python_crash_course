# (1) Building our first map with pygal
## import necessary modules
import pygal


## Create an instance of the World Map and assign to variable wm
wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

## Create the attributes to display the regions and countries on the chart
wm.add('North America', ['ca', 'mx', 'us'])  
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])  
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec','gf', 'gy',
		'pe', 'py', 'sr', 'uy', 've'])  

## Generate Chart with above attributes
wm.render_to_file('americas.svg')
