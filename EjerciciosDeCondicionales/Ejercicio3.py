numero1 = float(input("Introduce un número:"))
numero2 = float(input("Introduce un segundo número:"))

if numero2 == 0 :
    input("Error. El divisor no puede ser 0")
else:
    división = numero1 / numero2
    input(f"El resultado de la divión es: {división}")
