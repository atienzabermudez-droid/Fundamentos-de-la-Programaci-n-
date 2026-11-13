inversion = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual (en %): "))
años = int(input("Introduce el número de años: "))

for i in range(1, años + 1):
    inversion *= 1 + (interes / 100)
    print(f"Año {i}: {inversion:.2f} €")