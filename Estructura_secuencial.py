# promedio de tres numeros
numero_1 = int(input("ingrese el primer numero:"))
numero_2 = int(input("ingrese el segundo numero:"))
numero_3 = int(input("ingrese el tercer numero:"))

suma = numero_1 + numero_2 + numero_3
promedio = suma / 3
print ("el promedio de los tres numeros es ",promedio)

#ejecicio 1
# nota promedio entre 5 materias
nota_1 = int(input("ingrese la primer nota:"))
nota_2 = int(input("ingrese la segunda nota:"))
nota_3 = int(input("ingrese la tercera nota:"))
nota_4 = int(input("ingrese la cuarta nota:"))
nota_5 = int(input("ingrese la quinta nota:"))

suma = nota_1 + nota_2 + nota_3 + nota_4 + nota_5
promedio = suma / 5
print("el promedio de sus notas es :",promedio)

#ejercicio 2
"""Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""

alto = int( input("ingrese el alto de la pared: "))
Largo = int (input("Ingrese el largo de la pared: "))
valor_x_mts = int(input("ingrese el valor del mtr cuadrado pintado: "))

superf = alto * Largo 
costo = superf * valor_x_mts

print("Pintar ",superf," metros cuadrados, te sale ",costo," pesos")

#ejercicio 3
"""Un hincha de fútbol desea conocer la cantidad de puntos que su

equipo lleva acumulados en el campeonato, para ello recibe cada semana la

información de la cantidad total de partidos, desde el inicio del campeonato, que

el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

puntos."""

partidos_ganados = int(input("ingrese el total de partidos ganados: "))
partidos_empatados = int(input("ingrese el total de partidos empatados: "))
partidos_perdidos =int(input("ingrese el total de partidos perdidos: "))

puntos_acumulados = partidos_ganados * 3 +partidos_empatados * 1 + partidos_perdidos * 0 #los partidos perdidos no son necesarios xq no suman ptos
print("los puntos acumulados a la fecha son: ",puntos_acumulados)