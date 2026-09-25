cantidadDinero = float(input("Ingrese la cantidad de dinero depositado: "))
interesAnual = 4
años= 3
capitalFinal = cantidadDinero * (1 + interesAnual / 100) ** años
print(f"El capital final tras 3 años es: {capitalFinal:.2f}€")