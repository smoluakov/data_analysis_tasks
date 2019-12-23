import pygal
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):


	#возвращает код Pygal для заданной страны 
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	#Если старна не найдена вернуть None
	return None


