import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Elije un mes")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "Octubre", 
                                    "Febrero",
                                    "Noviembre",
                                    "Agosto"]) 
comboExample.grid(column=0, row=1)
comboExample.current(1)

app.mainloop()