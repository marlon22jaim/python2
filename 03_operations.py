set_a = {"col", "mex", "bol"}
set_b = {"pe", "bol", "arg", "ecu"}

# union de conjuntos
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# interseccion de los conjuntos o elementos en común
# imprime los elementos que tienen en comun los conjuntos
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)


# diferencia muestra los elementos de el primer conjunto quitandole los elementos que tenga el otro conjunto
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

set_c = set_b.difference(set_a)
print(set_c)
print(set_b - set_a)

# diferencia simetrica elimina los elementos que tengan en comun los conjuntos
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)
