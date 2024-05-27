# listas
Nombre_lista = [1,2,3,4,5,6]
#se identifica cada elemento por un indice que va desde el 0, para identificar el ultimo elemento se usa el -1
print(Nombre_lista[0])

#agregar un elemento
Nombre_lista.append("Fede")
print(Nombre_lista)

#eliminar
Nombre_lista.pop()

#ordenar Lista
Nombre_lista.sort()
Nombre_lista.sort(reverse=1) #orden descendente


# crear una lista de 5 nuemerosal azar entre el 1 al 9 sin repetidos

import random 
lista=[]
numero= random.randint(0,9)

while len(lista) < 5:
    if numero not in lista:
        lista.append(numero)
    numero = random.randint(0,9)
lista.sort()
print (lista)

#Tuplas
Nombre_Tupla =(4,5,6,7,8)

#diccionario
Nombre_Diccionario={"Nombre":"Fede","Apellido":"Cordoba"}
print(Nombre_Diccionario)

"""Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos."""

print ("ingrese 10 nombres de personas no repetidos")

lista_nombres = []

while len(lista_nombres) < 10:
    Nombre = input("ingrese un nombre")
    if Nombre not in lista_nombres:
        lista_nombres.append(Nombre) 
        print(lista_nombres)
    else: print("El nombre ya esta repetido") 