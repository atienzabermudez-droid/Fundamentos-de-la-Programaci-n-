numero = int(input("Introduce un número entero positivo: "))

for i in range(1, numero + 1, 2):
    if i == numero or i + 2 > numero:
        print(i)
    else:
        print(i, end=", ")