import time

h = time.strftime('%H')
m = time.strftime('%M')

def hora_de_ir_a_casa():
  if int(h) >= 19:
    print("Hora de ir a casa") 
  else:
    print("Quedan", 19 - h, ":", 60 - int(m),"para ir a casa")

hora_de_ir_a_casa()