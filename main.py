import problema1


'''
Hasta ahora hemos
trabajado con variables
que permiten almacenar un único valor
'''


edad = 12

altura = 1.79

nombre = "Juan"

estado = True

'''
En Python podemos 
usar una variable 
que almacena una 
colección de datos 
y luego accederla
usando un subindice
'''

# lista de enteros
lista1 = [10,5, 3, 9]

# lista decimales
lista2 = [1.78, 2.66, 1.55, 89.4, 6.9]

# lista de string
lista3 =  ["Lunes", "Martes", "Miercoles"]

'''
lista de elementos 
de distintos tipo
'''

lista4 = ["juan",45,1.92,False]



if __name__ == '__main__':

    '''
    cantidad de elementos de caada lista:
    '''
    print(len(lista1))
    print(len(lista2))
    print(len(lista3))
    print(len(lista4))

    print()
    print(lista1)
    lista1[0]= 1
    print()
    print(lista1)

    print(lista1[3])

    print()

    problema1.sumar_5_enteros()



