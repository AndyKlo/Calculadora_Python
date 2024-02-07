from sympy import symbols, Eq, solve, sqrt, Rational

def resolver_expresion_algebraica():
    # Paso 1: Ingresar la expresión algebraica y su igualdad
    expresion_str = input("Ingrese la expresión algebraica en términos de 'x': ")
    igualdad_str = input("Ingrese la igualdad de la expresión en términos de 'x': ")

    x = symbols('x')

    # Paso 2: Convertir las cadenas de entrada a expresiones simbólicas
    expresion = eval(expresion_str)
    igualdad = eval(igualdad_str)

    # Paso 3: Crear ecuación simbólica
    ecuacion = Eq(expresion, igualdad)

    # Paso 4: Resolver la ecuación
    solucion = solve(ecuacion, x)

    # Paso 5: Mostrar el resultado
    print(f"Expresión ingresada: {expresion_str} = {igualdad_str}")
    if solucion:
        print(f"La solución para x es: {solucion[0]}")
    else:
        print("La ecuación no tiene solución única.")

if __name__ == "__main__":
    resolver_expresion_algebraica()


