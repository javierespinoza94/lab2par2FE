#!/usr/bin/python3
import time
# importing os module
import os
from itertools import chain


def pedirNumeroEntero():

    correcto = False
    num = 0
    while(not correcto):
        try:
            num = int(
                input("Introduce un numero entero que sea uno de las opciones: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')

    return num


def perdirNombreString():

    nameFile = ''
    correcto = False

    while(not correcto):
        try:
            nameFile = input(
                "Introduce el nombre del archivo a procesar: ")
            correcto = True
        except ValueError:
            print('Error, introduce un string entero')

    return nameFile


salir = False
opcion = 0
while not salir:

    print('NOTA: Los archivos a especificar estan contenidos en la carpeta raiz de este proyecto ')
    print('***: -------------------------------------------------------------------------------- :***')

    print("1. Especifique el nombre de archivo que desea procesar:")
    print("2. Salir")

    print("Elige una opcion")

    opcion = pedirNumeroEntero()
    # inicia el tiempo de ejecucion
    start_time = time.time()
    if opcion == 1:
        # funcion que requiere y almacena el nombre del archivo por entrada de consola
        fileName = perdirNombreString()
        try:
            # store de caracteres
            nCharcs = 0
            # store de palabras unicas
            nUniqueWords = 0
            # store de numero de lineas
            nLines = 0
            # store del total de palabras
            nWords = 0
            # store para el total de espacios en blanco
            nSpaces = 0

            unique = []

            with open(fileName, 'r') as file:

                # loop para iterar el archivo linea por linea
                for line in file:
                    # usando las propiedades del modulo os
                    # usaremos linesep para separar las lineas por el caracter
                    line = line.strip(os.linesep)
                    wordslist = line.split()
                    for x in wordslist:
                        if x not in unique:
                            unique.append(x)

                    nLines = nLines + 1
                    nWords = nWords + len(wordslist)
                    nCharcs = nCharcs + \
                        sum(1 for c in line if c not in (os.linesep, ' '))
                    nSpaces = nSpaces + \
                        sum(1 for c in line if c not in (os.linesep, ' '))

            print('Numero de caracteres incluyendo espacios', nCharcs + nSpaces)
            print('Numero de lineas totales ', nLines)
            print('Numero de palabras totales', nWords)
            print('Numero de palabras unicas totales', len(unique))
            # termina el tiempo de ejecucion
            print("--- %s seconds ---" % (time.time() - start_time))
        except ValueError:
            print('Error, el archivo no se puede abrir o esta corrupto')
    elif opcion == 2:
        salir = True
    else:
        print("Introduce un numero entre 1 y 2")

print("Fin")
