class Vehiculo:
  def __init__(self, color,ruedas, puertas):
    self.color = color
    self.ruedas = ruedas
    self.puertas = puertas 
    
  def attributes(self):
    print("color: ", self.color, "Ruedas: ", self.ruedas, " puertas: ", self.puertas)
  
class Coche(Vehiculo):
  velocidad = 187
  cilindrada = 1600
  def attributes(self):
    print("color: ", self.color, "Ruedas: ", self.ruedas, " puertas: ", self.puertas, " Velocidad: ", self.velocidad, "Cilindrada: ", self.cilindrada)

coche1 = Coche("rojo", 4 , 4)

coche1.attributes()