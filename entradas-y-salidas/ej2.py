from pickle import *

class Vehiculo:

    def __init__(self, marca, ruedas):
        self.marca = marca
        self.ruedas = ruedas

camioneta = Vehiculo("Dodge", "2")


file = open('obj_vehiculo', 'w+b')

dump(camioneta, file)

file.seek(0)
new_camioneta = load(file)

print(new_camioneta)
file.close()