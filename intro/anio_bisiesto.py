def bisiesto(anio):
	print("bisiesto" if not anio % 4 and (anio % 100 or  not anio % 400) else "No es bisiesto")

bisiesto(int(input("ingrese un año (ej: 1993): ")))