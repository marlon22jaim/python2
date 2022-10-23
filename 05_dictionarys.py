"""
dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)


dict_v2 = {i: i*2 for i in range(1, 5)}
print(dict_v2)
"""
import random
countries = ["col", "mex", "bol", "pe"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100000000)

print(population)

population_v2 = {country: random.randint(
    1, 100000000) for country in countries}
print(population_v2)

names = ["nico", "marlon", "santi"]
ages = [12, 24, 98]
"""
{
    "nico":12,
    "marlon":24,
    "santi":98
}
"""
print(list(zip(names, ages)))
new_dictionary = {name: age for (name, age) in zip(names, ages)}
print(new_dictionary)