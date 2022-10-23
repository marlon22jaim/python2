# al ser un conjunto no imprime valores repetidos
set_countries = {"colombia", "mexico", "colombia", "bolivia"}
print(set_countries)
print(type(set_countries))

set_numbers = {1, 2, 2, 442, 21}
print(set_numbers)

set_types = {1, "hola", False, 12.12}
print(set_types)

set_from_string = set("hooola")
print(set_from_string)

set_from_tuples = set(("abc", "cbv", "as", "abc"))
print(set_from_tuples)

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)
