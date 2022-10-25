# try:
#     print(0/0)
# except ZeroDivisionError as error:
#     print(error)

# try:
#     assert 1 != 1, "Error, uno no es diferente de uno"
# except AssertionError as error:
#     print(error)

# try:
#     age = 10
#     if age < 18:
#         raise Exception("No se permiten menores de edad")
# except Exception as error:
#     print(error)


try:
    print(0/0)
    assert 1 != 1, "Error, uno no es diferente de uno"
    age = 10
    if age < 18:
        raise Exception("No se permiten menores de edad")

except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print("Hola")
