class Shit():
    def __init__():
        resolver_ecuacion_biseccion()

        
def ecuacion(x):
    #Define tu propia ecuación aquí
    return x**2 + 4

def resolver_ecuacion_biseccion(a, b, tolerancia=1e-6, max_iter=100):
    if ecuacion(a) * ecuacion(b) > 0:
        print("No se puede garantizar la existencia de una solución en el intervalo dado.")
        return None
    iteracion = 0
    while (b - a) / 2 > tolerancia and iteracion < max_iter:
        c = (a + b) / 2
        if ecuacion(c) == 0:
            return c
        elif ecuacion(c) * ecuacion(a) < 0:
            b = c
        else:
            a = c
        iteracion += 1

    return (a + b) / 2

# Ejemplo de uso
solucion = resolver_ecuacion_biseccion(4, 2)
if solucion is not None:
    print("Solución:", solucion)
else:
    print("No se encontró una solución.")
