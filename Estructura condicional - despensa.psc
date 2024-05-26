Algoritmo despensa

	Escribir "cuantas botellas de leche compra?"
	leer compra
	Si compra <= 24  Entonces
		SI compra >=12 Entonces
			Pagar <- compra * 1000 * 0.9  //aplica un 10% de descuento
		SiNo
			pagar <- compra * 1000
		FinSi
	SiNo
		pagar <- compra * 1000 * 0.85 //aplica un 15% de descuento
	Fin Si
	
	escribir "El cliente es jubilado: (Si - No)"
	Leer Jubilado
	si Jubilado = "Si" Entonces
		escribir "El cliente debe pagar: ", pagar * 0.9   //aplica un 10% de descuento
	SiNo
		Escribir "El cliente debe pagar: ", pagar
	FinSi
	
FinAlgoritmo
