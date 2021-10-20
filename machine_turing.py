"""
Programa que ejecuta una máquina de turing con sus operaciones basicas

AUTOR: Fabricio Pafumi
CATEDRA: Fundamentos teoricos de la informatica
UNIVERSIDAD DE LA PATAGONIA SAN JUAN BOSCO
"""

import csv
import time
from operaciones_turing import operaciones_turing as ot

def leer_csv():
    with open('./machines/suma_binaria.csv', newline="") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=";", quotechar='|')
        for row in spamreader:
            yield row

def cargar_csv():
    filas = []
    for fila_pura in leer_csv():
        fila = fila_pura
        filas.append(fila)
    return filas 

def cargar_diccionario(filas):
    diccionario = []
    for fila in filas.pop(0):
        if(fila != ''):
            diccionario.append(fila)
    return diccionario, filas

def cargar_estados(filas):
    estados = []
    for fila in filas:
        estados.append(fila.pop(0))
    return estados

def dibujar_indicador(indice):
    indicador = ""
    for i in range(0,indice):
        indicador = indicador + " "
    indicador = indicador + "▲"
    return indicador

def recorrer_tabla(filas,diccionario,estados,op_turing):
    indice_estado_actual = 0
    estado_actual = estados[indice_estado_actual]
    
    caracter_actual = op_turing.get_caracter_actual()
    indice_caracter_actual = diccionario.index(caracter_actual,0,diccionario.__len__())
    fila_actual = filas[indice_estado_actual]
    sep = fila_actual[indice_caracter_actual].split("/")

    while((sep[0] != op_turing.get_caracter_vacio()) or (sep[1] != op_turing.get_caracter_vacio())):
        time.sleep(2)
        mensaje = op_turing.operation(sep[0])
        print("OPERACION: {}".format(mensaje))
        print("{}".format(op_turing.get_cinta()))
        print("{}".format(dibujar_indicador(op_turing.get_indice_cinta())))
        indice_estado_actual = estados.index(sep[1],0,estados.__len__())
        caracter_actual = op_turing.get_caracter_actual()
        try:
            indice_caracter_actual = diccionario.index(
                caracter_actual, 0, diccionario.__len__())
        except ValueError as ve:
            pass
        fila_actual = filas[indice_estado_actual]
        sep = fila_actual[indice_caracter_actual].split("/")

operaciones = ot(input("Ingrese la cinta: "))
print("{}".format(operaciones.get_cinta()))
print("{}".format(dibujar_indicador(operaciones.get_indice_cinta())))

filas_puras = cargar_csv()
diccionario,filas = cargar_diccionario(filas_puras)
estados = cargar_estados(filas)

recorrer_tabla(filas,diccionario,estados,operaciones)
