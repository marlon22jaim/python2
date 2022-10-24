def increment(x):
    return x + 1


increment_v2 = lambda x: x + 1
print(increment(90))
print(increment_v2(90))

full_name = lambda name,last_name: f"Full name es {name.title()} {last_name.title()}"

print(full_name("marlon", "jaimes rangel"))