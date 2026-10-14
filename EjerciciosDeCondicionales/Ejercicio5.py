edad = int(input("Introduce la edad del usuario:"))
ingresos = float(input("Introduce sus ingresos mensuales:"))

if edad > 16 and ingresos >= 1000 :
    print("El usuario si puede tributar")
else:
    print("El usuario no puede tributar")