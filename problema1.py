def sumar_5_enteros():
    # definición de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los números:
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese el número " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # Sumamos los números
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los elementos de las lista son:")
    for numero in lista:
        print(numero, end=', ')

    print("\nLasuma de todos sus elementos es:")
    print(suma)


