nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M para mujer, H para hombre): ")

if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"

print("Te corresponde el grupo " + grupo)