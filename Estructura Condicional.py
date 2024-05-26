# rama verdadera
importe = float(input("ingrese el importe a evaluar:"))
if importe >10000:
    print("debe registrar su DNI")
print("gracias por su compra")

#rama verdadera y falsa
edad = int(input("ingrese su edad: "))
if edad >= 18:
    print("ud es mayor de edad")
else:
    print("ud es menor de edad")

# AND
edad = int(input("ingrese su edad: "))
if edad>= 18 and edad< 65:
    print("felicitaciones! se le ha otrogado el credido")
else: print("no es posible otorgar el credito")

# OR
#identifica el fin de semana

dia = input("ingrese el dia de la semana ")
if dia == "Sabado" or dia =="domingo":
    print("Feliz fin de semana")
else: print("hay que ir a la escuela")

