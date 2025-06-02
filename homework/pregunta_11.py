"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()

    # Crear un diccionario para almacenar las sumas
    letter_sums = {}

    # Procesar cada línea
    for line in data:
        # Separar las columnas
        columns = line.strip().split("\t")
        col2_value = int(columns[1])  # Columna 2 (valor numérico)
        col4_letters = columns[3].split(",")  # Columna 4 (lista de letras)

        # Sumar el valor de la columna 2 a cada letra de la columna 4
        for letter in col4_letters:
            if letter in letter_sums:
                letter_sums[letter] += col2_value
            else:
                letter_sums[letter] = col2_value

    # Ordenar el diccionario por clave (alfabéticamente)
    result = dict(sorted(letter_sums.items()))

    return result

# Llamar a la función y probar
print(pregunta_11())