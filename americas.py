import pygal
from pygal.maps.world import World

wm = World()
wm.title = 'North , South and Central America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Canral America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
