anio = int(input("Ingrese un anio: "))

if anio % 4 != 0: 
	print("bisiesto")
elif anio % 4 == 0 and anio % 100 != 0: 
	print("bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 != 0: 
	print("No es bisiesto")
elif anio % 4 == 0 and anio % 100 == 0 and anio % 400 == 0: 
	print("Es bisiesto")