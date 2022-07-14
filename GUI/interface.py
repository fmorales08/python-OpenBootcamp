from cgitb import text
import tkinter
ventana = tkinter.Tk()
seleccion = tkinter.IntVar()
R1 = tkinter.Radiobutton(ventana, text="opcion 1", variable=seleccion,value=1).pack( anchor= tkinter.W)
R2 = tkinter.Radiobutton(ventana, text="opcion 2", variable=seleccion,value=2).pack( anchor= tkinter.W)
R3 = tkinter.Radiobutton(ventana, text="opcion 3", variable=seleccion,value=3).pack( anchor= tkinter.W)
label = tkinter.Label(ventana)
label.pack()
def reset():
    seleccion.set(5)
tkinter.Button(ventana, text="Reiniciar", command=reset).pack()
ventana.mainloop()