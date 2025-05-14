"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    total = 0.0
    ruta_archivo = "files\input\data.csv" 
    separador='\t'
    tiene_encabezado=False
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        if tiene_encabezado:
            next(f)
        for linea in f:
            campos = linea.strip().split(separador)
            total += int(campos[1])
    return int(total)




print(pregunta_01())

"""
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
