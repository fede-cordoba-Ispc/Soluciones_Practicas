
#Mostrar los números desde el 0 al número solicitado al usuario (input)
numero= int(input("ingrese un numero"))
for i in range(numero +1):
    print(i)

#Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)

numero= int(input("ingrese un numero"))
for i in range(numero +1):
    if i % 2 == 0:
       print(i)


"""Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
3x1=3
3x2=6
3x3=9
…. y así hasta 10

5.1 Resuelva este problema utilizando un mientras y de modo que por la salida se emita la tabla tal como se propone.
5.2 Resuelva este problema utilizando un para y de modo que por la salida se emita la tabla tal como se propone."""

Tabla = int(input("Que tabla quiere generar"))
for i in range(1,11):

    print(Tabla,"X",i," = ",i*Tabla)

Tabla = int(input("Que tabla quiere generar"))
c=1
while c <11:
    print(Tabla,"X",c," = ",c*Tabla)
    c= c + 1