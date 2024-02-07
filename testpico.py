import tkinter as tk
from tkinter import ttk
from sympy import sympify, latex

def on_entry_change(*args):
    try:
        # Intentar interpretar la entrada como una expresión matemática
        expresion = sympify(entry_var.get())

        # Simplificar la expresion
        expresion_simplificada = expresion.simplify()

        # Convertir la expresión simplificada a LaTeX
        expresion_latex = latex(expresion_simplificada)

        # Actualizar la etiqueta con la expresión simplificada
        label_var.set(expresion_latex)
    except:
        # Si la entrada no puede ser interpretada como una expresión matemática, limpiar la etiqueta
        label_var.set("")

root = tk.Tk()

# Crear una variable de control StringVar para la entrada
entry_var = tk.StringVar()
entry_var.trace("w", on_entry_change)

# Crear una variable de control StringVar para la etiqueta
label_var = tk.StringVar()

# Crear un widget Entry y un widget Label
entry = ttk.Entry(root, textvariable=entry_var)
label = ttk.Label(root, textvariable=label_var)

entry.pack()
label.pack()

root.mainloop()