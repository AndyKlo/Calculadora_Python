import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from sympy import symbols, sqrt, latex, simplify, sympify

def mostrar_expresion():
    # Obtener la expresión ingresada por el usuario
    expresion_usuario = entrada_expresion.get()

    try:
        # Interpretar la expresión ingresada como una expresión matemática de SymPy
        expresion_sympy = sympify(expresion_usuario)

        # Obtener la representación en formato LaTeX de la ecuación original
        expresion_latex_original = latex(expresion_sympy)

        # Simplificar la expresión ingresada
        expresion_simplificada = simplify(expresion_sympy)

        # Obtener la representación en formato LaTeX de la ecuación simplificada
        expresion_latex_simplificada = latex(expresion_simplificada)

        # Crear una figura de Matplotlib para la ecuación original
        fig_original = Figure(figsize=(5, 2), dpi=100)
        ax_original = fig_original.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
        ax_original.axis('off')
        ax_original.text(0.5, 0.5, f"${expresion_latex_original}$", size=20, ha='center', va='center')

        # Crear una figura de Matplotlib para la ecuación simplificada
        fig_simplificada = Figure(figsize=(5, 2), dpi=100)
        ax_simplificada = fig_simplificada.add_axes([0, 0, 1, 1], frameon=False, aspect=1)
        ax_simplificada.axis('off')
        ax_simplificada.text(0.5, 0.5, f"${expresion_latex_simplificada}$", size=20, ha='center', va='center')

        # Limpiar el lienzo anterior (si existe)
        for widget in frame_expresion.winfo_children():
            widget.destroy()

        # Crear el lienzo de Tkinter para la ecuación original
        canvas_original = FigureCanvasTkAgg(fig_original, master=frame_expresion)
        canvas_widget_original = canvas_original.get_tk_widget()
        canvas_widget_original.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Crear el lienzo de Tkinter para la ecuación simplificada
        canvas_simplificada = FigureCanvasTkAgg(fig_simplificada, master=frame_expresion)
        canvas_widget_simplificada = canvas_simplificada.get_tk_widget()
        canvas_widget_simplificada.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    except Exception as e:
        # Manejar errores al procesar la expresión
        etiqueta_error.config(text=f"Error: {str(e)}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Expresión Matemática")

# Crear un cuadro de entrada para que el usuario ingrese la expresión
entrada_expresion = ttk.Entry(ventana, width=30)
entrada_expresion.pack(pady=10)

# Crear botón para mostrar la expresión
boton_mostrar = ttk.Button(ventana, text="Mostrar Expresión", command=mostrar_expresion)
boton_mostrar.pack(pady=10)

# Crear un marco para mostrar la expresión
frame_expresion = ttk.Frame(ventana)
frame_expresion.pack(pady=10)

# Etiqueta para mostrar errores
etiqueta_error = ttk.Label(ventana, foreground="red")
etiqueta_error.pack(pady=10)

# Iniciar el bucle de eventos de Tkinter
ventana.mainloop()
#ecuaciones random
# 2**x + 3*x**2 - 5
#2 incognitas sqrt(((a+322**x)/(a-log(x**2)))**2, 2)
#Terminos semejantes: -(((3*(x**2))+((-2*x)+(5*(x**2)))-(9*x)))
# terminos semejantes con fraccion: (((x**2)+(5*x)+6)/(x+2))