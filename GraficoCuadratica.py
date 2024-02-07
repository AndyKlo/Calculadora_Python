import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from sympy import symbols, Eq, solve, I

class EcuacionCuadratica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora - Ecuación Cuadrática")

        # Crear un marco principal
        self.frame = ttk.Frame(root)
        self.frame.pack()

        # Entrada para los coeficientes de la ecuación cuadrática
        ttk.Label(self.frame, text="Coeficiente a:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = ttk.Entry(self.frame, width=10)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Coeficiente b:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_b = ttk.Entry(self.frame, width=10)
        self.entry_b.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.frame, text="Coeficiente c:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_c = ttk.Entry(self.frame, width=10)
        self.entry_c.grid(row=2, column=1, padx=5, pady=5)

        # Botón para mostrar la gráfica
        boton_mostrar = ttk.Button(self.frame, text="Mostrar Gráfica", command=self.mostrar_grafica)
        boton_mostrar.grid(row=3, column=0, columnspan=2, pady=10)

    def mostrar_grafica(self):
        # Obtener coeficientes de la ecuación cuadrática
        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        # Crear una expresión cuadrática y resolverla
        x = symbols('x')
        ecuacion = Eq(a * x**2 + b * x + c, 0)
        soluciones = solve(ecuacion, x)

        # Filtrar soluciones complejas y obtener solo las partes reales
        soluciones_reales = [sol.evalf() for sol in soluciones if sol.is_real]

        if not soluciones_reales:
        # Mostrar un mensaje si no hay soluciones reales
            tk.messagebox.showinfo("Advertencia", "La ecuación cuadrática no tiene soluciones reales.")
            return
        # Convertir el mínimo y máximo a números de punto flotante
        min_solucion = float(min(soluciones_reales))
        max_solucion = float(max(soluciones_reales))

        # Crear una figura para el gráfico
        fig, ax = plt.subplots()

        # Graficar la ecuación cuadrática
        x_vals = np.linspace(min_solucion - 2, max_solucion + 2, 100)
        y_vals = a * x_vals**2 + b * x_vals + c
        ax.plot(x_vals, y_vals, label='Ecuación Cuadrática')

        # Resaltar las soluciones en el gráfico
        ax.scatter(soluciones_reales, [0, 0], color='red', label='Soluciones')

        # Configurar el gráfico
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()

        # Mostrar el gráfico en la interfaz
        canvas = FigureCanvasTkAgg(fig, master=self.frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=4, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = EcuacionCuadratica(root)
    root.mainloop()
