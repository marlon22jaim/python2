def find_volume(length=1, width=1, depth=1):
    return length * width * depth


def find_volume2(length=1, width=1, depth=1):
    return length * width * depth, width, "hola"


result = find_volume(20, 30, 4)
print(result)

result2 = find_volume(width=30)
print(result2)

result3 = find_volume()
print(result3)

result4 = find_volume2(20, 30, 4)
print(result4)

result5 = find_volume2(20, 30, 4)
print(result5[2])

result, width, text = find_volume2(length=50)
print(result)
print(width)
print(text)
