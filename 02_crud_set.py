set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)

print("col" in set_countries)
print("pe" in set_countries)

# add

set_countries.add("pe")
print(set_countries)
set_countries.add("pe")
print(set_countries)

# update permite agregar otros conjuntos y nuestro conjunto deseado
set_countries.update({"arg", "ecua", "pe"})
print(set_countries)

# remove elimina el elemento del conjunto deseado pero si este elemento no existe muestra un error
set_countries.remove("col")
print(set_countries)
set_countries.remove("arg")
print(set_countries)

# discard elimina el elemento del conjunto deseado y si este no existe no hace nada
set_countries.discard("arg")
print(set_countries)


# pop elimina un dato aleatorio del conjunto y si el conjunto esta vacio lanza un error
set_countries.pop()
print(set_countries)

# clear elimina todos los datos del conjunto
set_countries.clear()
print(set_countries)
print(len(set_countries))
