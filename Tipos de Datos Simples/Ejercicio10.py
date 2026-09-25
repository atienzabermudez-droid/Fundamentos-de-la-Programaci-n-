numPayasos = int(input("Ingrese el número de payasos vendidos en el último pedido: "))
numMuñecas = int(input("Ingrese el número de muñecas vendidas en el último pedido: "))
pesoPayasos = numPayasos * 112
pesoMuñecas = numMuñecas * 75
pesoTotal = pesoPayasos + pesoMuñecas
print(f"El peso total del paquete es: {pesoTotal} gramos")