#!/usr/bin/python3
import time


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
            print('Error')

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

    if opcion == 1:
        # inicia el tiempo de ejecucion
        start_time = time.time()
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
            with open(fileName, 'r') as archivo:
                for linea in archivo:
                    # incrementamos el numero de lineas del archivo
                    nLines += 1
                    # declaramos la variable word
                    # y le asignamos el valor 'Y'
                    # porque cada file comienza con
                    # una palabra o caracter
                    unique = []  # diccionario para guardar ocurrencia de palabras
                    word = 'Y'
                    for letra in linea:
                        unique.append(letra)
                        if letra not in unique:
                            unique += 1
                        if (letra != ' ' and word == 'Y'):

                            # incrementamos el contador de palabras en 1
                            nWords += 1
                            # asignando valor N a
                            # a la varibale word porque hasta
                            # espacio no encontrará
                            # una palabra no se puede completar
                            word = 'N'
                        elif (letra == ' '):
                            # incrementamos el contador de los espacios en blanco en uno
                            nSpaces += 1
                            # assigning value Y to
                            # variable word because after
                            # white space a word
                            # is supposed to occur
                            word = 'Y'

                        for i in letra:
                            # condicion para evaluar si es espacio en blanco o una nueva linea
                            if(i != " " and i != "\n"):
                                # incrementamos el contador de los espacios en uno
                                nCharcs += 1

            print(
                'Numero de caracteres incluyendo espacios', nCharcs + nSpaces)
            print('Numero de lineas', nLines)
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
