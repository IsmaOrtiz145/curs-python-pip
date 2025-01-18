"""Principal"""
import utils
import read_csv
import chart

def main():
    """Programa principal"""
    ruta = 'data.csv'
    data = read_csv.read_csv(ruta)

    country = input('Selecciona el país: ')
    result = utils.population_by_countries(data, country)

    if len(result) > 0:
        country = result[0]
        keys, values = utils.get_population(country)
        chart.generate_bar_chart(keys, values)

if __name__ == '__main__':
    main()
