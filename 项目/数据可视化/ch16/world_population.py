import json
import pygal
from country_codes import get_country_code
from pygal.style import RotateStyle, LightColorizedStyle

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        # print(country_name + ': ' + str(population))
        # if code:
            # print(code + ": " + country_name)
        # else:
            # print('ERROR - ' + country_name)
        if code:
            cc_populations[code] = population
            
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# ~ print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
            
wm_style = RotateStyle('#336699', base_stle=LightColorizedStyle)
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'World population in 2010, by country'
# ~ wm.add('2010', cc_populations)
wm.add('0-10m',cc_pops_1)
wm.add('10-1bm',cc_pops_2)
wm.add('>1bm',cc_pops_3)

wm.render_to_file('world_population.svg')

