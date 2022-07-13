class Alumno:
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota
  def estado(self):
    if self.nota >= 4:
      return print(self.nombre, "Nota:" , self.nota,"Aprobado")
    else: 
      return print(self.nombre, "Nota:" , self.nota,"No aprobado")

a1 = Alumno("Fabian", 4 )

a1.estado()