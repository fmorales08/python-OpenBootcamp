paises = []

for i in range(5):
  pais = input("Ingrese un país: ")
  paises.append(pais)

paises = list(set(paises))
paises.sort()
print(paises)