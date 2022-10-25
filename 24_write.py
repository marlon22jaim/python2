
# reescribe por completo el archivo y solo le agrega las nuevas lineas
# with open("./text.txt","w+") as file:
#     for line in file:
#         print(line)
#     file.write("Nueva linea por codigo")

with open("./text.txt", "r+") as file:
    for line in file:
        print(line)
    file.write("Nueva linea por codigo\n")
    file.write("Nueva linea por codigo 2\n")
