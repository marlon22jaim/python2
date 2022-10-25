import utils

data = [
    {
        "Country": "Colombia",
        "Population": 4000
    },
    {
        "Country": "Mexico",
        "Population": 7000
    },
    {
        "Country": "Bolivia",
        "Population": 2000
    }
]


def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input("escribe el pais: ")
    result = utils.population_by_country(data, country)
    print(result)


if __name__ == "__main__":
    run()
