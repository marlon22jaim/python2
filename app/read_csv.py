import csv
from email import header


def read_csv(path):
    with open(path, "r") as csvfile:
        # obteniendo los valores del csv
        reader = csv.reader(csvfile, delimiter=",")
        # obteniendo los valores del encabezado del csv
        header = next(reader)
        data = []
        for row in reader:
            # en este for podemos ir linea a linea del csv
            # usamos zip para unir la cabecera con el cuerpo del csv linea a linea
            iterable = list(zip(header, row))

            # convertimos la tupla en diccionarios llave valor
            country_dict = {key: value for key, value in iterable}
            # creamos una lista con diccionarios llave valor
            data.append(country_dict)

        return data


if __name__ == "__main__":
    data = read_csv("./app/data.csv")
    print(data[0])
    print(data[1])
    print(data[2])
    # print(data)

