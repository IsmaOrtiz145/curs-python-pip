"""Modulos"""
def get_population(country_dict):
    """Obtiene la poblacion de un pais"""
    population_dict = {
        '2022': int(country_dict['2022 Population']),
        '2020': int(country_dict['2020 Population']),
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    }

    #Se retorna de esta forma por que es lo que se necesita para la grafica
    keys = population_dict.keys()
    values = population_dict.values()

    return keys , values

def population_by_countries(data, country):
    """Devuelve la poblacion de un pais pasado como parametro"""
    aux = list(filter(lambda item: item['Country/Territory'] == country, data))
    return aux
