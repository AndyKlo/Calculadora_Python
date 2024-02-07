import tkinter as tk
from tkinter import ttk, messagebox

class Ecuaciones(tk.Tk):
    class EcuacionBase:
        def __init__(self, root, tipo):
            self.root = root
            self.root.title(f"{tipo.capitalize()} - Calculadora")
            self.root.geometry("400x300")

            self.label = ttk.Label(root, text=f"Calculadora de Ecuación {tipo.capitalize()}", font=("Arial", 14))
            self.label.pack(pady=10)

    class EcuacionLineal(EcuacionBase):
        def __init__(self, root):
            super().__init__(root, "Lineal")

    class EcuacionExponencial():
        def __init__(self, root):
            self.root = root
            self.root.title("Calculadora - Ecuación Exponencial")
            self.frame = ttk.Frame(
                self.root, relief="solid", padding=(10, 10), borderwidth=2, style="My.TFrame"
            )
            self.frame.pack()
            self.label_igualdad = ttk.Label(
                self.frame, text=f'Resolver Ecuación por igualdad', font=("Arial", 14)
            )
            #Entrada de datos
            self.label_igualdad.pack(pady=5)
            self.label_a = ttk.Label(self.frame, text="Ingrese la expresión:")
            self.label_a.pack()
            self.entry_a = ttk.Entry(self.frame, width=10)
            self.entry_a.pack()
            self.label_b = ttk.Label(self.frame, text="Ingrese la igualdad: ")
            self.label_b.pack()
            self.entry_b = ttk.Entry(self.frame, width=10)
            self.entry_b.pack()
            boton_mostrar = ttk.Button(self.frame, text="Calcular", command=None)
            boton_mostrar.pack()

            # Crear un marco para mostrar la expresión y la solución
            self.frame_expresion = ttk.Frame(root)
            self.frame_expresion.pack(pady=10)

            # Etiqueta para mostrar errores
            self.etiqueta_error = ttk.Label(self.frame, foreground="red")
            self.etiqueta_error.pack(pady=10)

    class EcuacionTrascendental(EcuacionBase):
        def __init__(self, root):
            self.root = root
            self.root.title("Calculadora - Ecuacion Trascendental")
            self.frame = tk.Frame(self.root)
            self.frame.pack()
            label_expresion = ttk.Label(self.frame, text="Ingrese la expresión:")
            label_expresion.pack()
            boton_mostrar = ttk.Button(self.frame, text="Mostrar Expresión", command=None)
            boton_mostrar.pack()
    
    class Inecuacion(EcuacionBase):
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
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Calculadora - Ecuación Exponencial")
        self.current_calculator = None

        # Menú de navegación
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Ecuación Exponencial por defecto
        self.mostrar_calculadora("Exponencial")

    def mostrar_calculadora(self, tipo):
        type_of = self.TIPOS_ECUACIONES.get(tipo)
        if type_of is None:
            raise ValueError(f"La calculadora {tipo} no existe.")
        calculadora = type_of(self)  # Pasa la ventana principal, no el frame
        self.current_calculator = tipo
        self.build_menu()

    def build_menu(self):
        self.menu_bar.delete(0, 'end')
        ecuaciones_menu = tk.Menu(self.menu_bar, tearoff=0)
        for tipo in self.TIPOS_ECUACIONES.keys():
            ecuaciones_menu.add_command(
                label=f"Ecuación {tipo}",
                command=lambda ct=tipo: self.mostrar_calculadora(ct),
                state='disabled' if tipo == self.current_calculator else 'normal'
            )
        self.menu_bar.add_cascade(label="Ecuaciones", menu=ecuaciones_menu)

    def switch_calculator(self, tipo):
        # Agrega la calculadora actual de nuevo a TIPOS_ECUACIONES
        self.TIPOS_ECUACIONES[self.current_calculator] = self.current_calculator.__class__
        self.mostrar_calculadora(tipo)

    TIPOS_ECUACIONES = {
            "Lineal": EcuacionLineal,
            "Exponencial": EcuacionExponencial,
            "Trascendental": EcuacionTrascendental,
            "Diferencial": Inecuacion,
            "Integral": "Integral",
            "Funcional": "Funcional",
        }
class CalculadoraGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x480")
        self.title("Resolución de ecuaciones")
        self.resizable(False, False)
class Cientifica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x480")
        self.title("Resolución de ecuaciones")
        self.resizable(False, False)
class CalculadoraTrigonometrica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x480")
        self.title("Resolución de ecuaciones")
        self.resizable(False, False)

class MainApp(tk.Tk):
    CALCULATORS = {
        "Cinetífica": Cientifica,
        "Ecuaciones": Ecuaciones,
        "gráfica": CalculadoraGrafica,
        #"calculadora de matrices": "CalculadoraMatrices",
        #"finanzas": "CalculadoraFinanzas",
    }
    def __init__(self):
        super().__init__()
        self.title("calculadora científica y resolución de ecuaciones EasterEgg") #Calculadora de integrales, derivadas y ecuaciones.
        self.geometry("220x220")
        self.resizable(False, True)
        self.bind('<Escape>', self.exit)

        ttk.Label(self, text="Seleccione una calculadora:", font=("Arial", 12, "bold"),
            foreground="blue", background="yellow", justify="center", relief="solid"
        ).pack(pady=10)

        for type in self.CALCULATORS.keys():
           ttk.Button(self, text=f"Calculadora {type.capitalize()}", 
                command=lambda ct=type: self.after(0, lambda: self.run_calculator(ct)),
            ).pack(pady=12)
           
    def run_calculator(self, type):
        typeOfCalc = self.CALCULATORS.get(type)
        if typeOfCalc is None:
            raise ValueError(f"La calculadora {type} no existe.")
        calculator = typeOfCalc()
        calculator.mainloop()

    def center_window(self):
        self.update_idletasks()  # Actualiza las tareas de la ventana
        window_width = self.winfo_width()
        window_height = self.winfo_height()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()-200
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.geometry(f"+{position_right}+{position_top}")

    def exit(self, event):
        if messagebox.askyesno("Confirmar", "¿Cerrar calculadora?"):
            self.destroy()

if __name__ == "__main__":
    app = MainApp()
    app.center_window()
    app.mainloop()

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import Symbol, exp

# Agregar los botones del 1 al 9
for i in range(1, 10):
    ttk.Button(frame_left_top, text=str(i), command=lambda num=i: self.button_clicked(num)).grid(
        row=2 + (i - 1) // 3, column=(i - 1) % 3, sticky="news", padx=5, pady=5
    )
for i, text in enumerate(['0', '.']):
    ttk.Button(frame_left_top, text=text, command=lambda num=text: self.button_clicked(num)).grid(
        row=5, column=i, sticky="news", padx=5, pady=5
    )
    --------------------------------------------
# Parte derecha abajo (40% de la pantalla)
frame_right_bottom = ttk.Frame(paned_window_right)
paned_window_right.add(frame_right_bottom)

# Agrega aquí los widgets para la parte derecha abajo según tus necesidades
# Ejemplo:
ttk.Label(frame_right_bottom, text="Parte Derecha Abajo").grid(row=0, column=0, sticky="news")


# Division Vertical
paned_window_right = ttk.PanedWindow(self, orient=tk.VERTICAL)
paned_window_right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# Parte derecha arriba (60% de la pantalla)
frame_right_top = ttk.Frame(paned_window_right)
paned_window_right.add(frame_right_top)

# Agrega aquí los widgets para la parte derecha arriba según tus necesidades
# Ejemplo:
ttk.Label(frame_right_top, text="Parte Derecha Arriba").grid(row=0, column=0, sticky="news")

# Widget PanedWindow división vertical
paned_window_left = ttk.PanedWindow(self, orient=tk.VERTICAL)
paned_window_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
# Parte izquierda arriba
frame_left_top = ttk.Frame(paned_window_left)
paned_window_left.add(frame_left_top)
"""