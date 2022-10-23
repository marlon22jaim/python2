import random

countries = ["col", "mex", "bol", "pe"]

population = {country: random.randint(1, 100) for country in countries}
print(population)

result = {country:populationn for (country, populationn) in population.items() if populationn > 40}
print(result)

text = "hola, Soy Marlon"
unique = {c: c.upper() for c in text if c in "aeiou"}
print(unique)