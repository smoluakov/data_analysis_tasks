import json
import pygal
from pygal.maps.world import World
from country_codes import get_country_code
from pygal.style import RotateStyle



#список заполняеться данными
filename = 'population_data.json'
with open(filename) as f:
	pop_data = json.load(f)


#вывод население каждой страны за 2010 год
cc_population = {}
for pop_dict in pop_data:

	if pop_dict['Year'] == '2010':

		country_name = pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
	
		code = get_country_code(country_name)

		if code:
			cc_population[code] = population 
			#print(code +":" + str(population))

			#группровка стран по 3 уровням населения
			cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
			for cc, pop in cc_population.items():
				if pop < 10000000:
					cc_pops_1[cc] = pop
				elif pop < 1000000000:
					cc_pops_2[cc] = pop
				else:
					cc_pops_3[cc] = pop


#проверка количесва стран в каждом слое
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))



wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = 'World Population in 2010'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

#wm.add('2010', cc_population)

wm.render_to_file('world_population.svg')

		
