cantidad=int(input("Introduce una cantidad a invertir: "))
interes=float(input("Introduce el interés anual (porcentaje): "))
años=int(input("Introduce el número de años: "))
capital=cantidad*(1+interes/100)**años
print(f"El capital final tras {años} años es: {capital}")