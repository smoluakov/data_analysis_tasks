import pygal
from pygal.maps.world import World

wm = World()
wm.title = 'North , South and Central America'

wm.add('North America', {'ca': 34126000, 'mx': 309349000, 'us': 113423000})


wm.render_to_file('na_populaton.svg')