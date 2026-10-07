Nombre = input("Introduce el nombre del producto:")
Precio = float(input("Introduce también su precio:"))
NumUnidades = int(input("Introduce también el número de unidades del producto:"))
total = Precio * NumUnidades
print(f"{Nombre}: {Precio:09.2f} {NumUnidades:03d} {total:011.2f}")
