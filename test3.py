import tkinter as tk
from tkinter import ttk
from sympy import Symbol, exp
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class EcuacionExponencial:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - Ecuación Exponencial")

        # Crear un marco principal
        self.frame = ttk.Frame(root)
        self.frame.pack()

        # Entrada para la ecuación
        self.entrada_ecuacion = ttk.Entry(self.frame, width=30)
        self.entrada_ecuacion.pack(pady=10)

        # Botón para mostrar la expresión
        boton_mostrar = ttk.Button(self.frame, text="Mostrar Expresión", command=self.mostrar_expresion)
        boton_mostrar.pack()

        # Crear un marco para mostrar la expresión y la solución
        self.frame_expresion = ttk.Frame(root)
        self.frame_expresion.pack(pady=10)

        # Etiqueta para mostrar errores
        self.etiqueta_error = ttk.Label(self.frame, foreground="red")
        self.etiqueta_error.pack(pady=10)

    def mostrar_expresion(self):
        # Limpiar el marco antes de mostrar la nueva expresión
        for widget in self.frame_expresion.winfo_children():
            widget.destroy()

        ecuacion = self.entrada_ecuacion.get()
        x = Symbol('x')

        try:
            expresion = exp(ecuacion)
            x_vals = np.linspace(0, 10, 100)
            solucion = [expresion.subs(x, val) for val in x_vals]
            
            self.mostrar_grafico(solucion)

            # Etiqueta para mostrar la expresión
            ttk.Label(self.frame_expresion, text=f"Ecuación: {expresion}").pack()

            # Etiqueta para mostrar la solución
            ttk.Label(self.frame_expresion, text=f"Solución para x=1: {expresion.subs(x, 1)}").pack()

            # Limpiar el mensaje de error si hubo alguno anteriormente
            self.etiqueta_error.config(text="")
        except Exception as e:
            # Mostrar mensaje de error si la ecuación no es válida
            self.etiqueta_error.config(text=f"Error: {str(e)}")
            print(e)

    def mostrar_grafico(self, solucion):
        # Crear una figura para el gráfico
        fig, ax = plt.subplots()

        # Graficar la solución
        ax.plot(np.linspace(0, 10, 100), solucion, label='Solución')

        # Configurar el gráfico
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.legend()

        # Mostrar el gráfico en la interfaz
        canvas = FigureCanvasTkAgg(fig, master=self.frame_expresion)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = EcuacionExponencial(root)
    root.mainloop()
