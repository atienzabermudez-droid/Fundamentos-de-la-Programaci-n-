PizzaVegetariana = input("¿Quieres pizza vegetariana?:")

if PizzaVegetariana.lower() == "si" :
    print ("Pimiento / Tofu")
    Ingredientes = input("¿Qué ingrediente quieres aparte del tomate y la mozarella?:")

    if Ingredientes.lower() == "tofu":
        print("Has elegido una pizza vegetariana")
        print("Tus ingredientes son: tomate, mozarella y tofu")
    else:
        print("Has elegido una pizza vegetariana")
        print("Tus ingredientes son: tomate, mozarella y pimiento")

else:
    print ("Peperoni / Jamón / Salmón")
    Ingredientes = input("¿Qué ingrediente quieres aparte del tomate y la mozarella?:")

    if Ingredientes.lower() == "peperoni":
        print("Has elegido una pizza  no vegetariana")
        print("Tus ingredientes son: tomate, mozarella y peperoni")
    elif Ingredientes.lower() == "jamón":
        print("Has elegido una pizza no vegetariana")
        print("Tus ingredientes son: tomate, mozarella y jamón")
    else:
        print("Has elegido una pizza no vegetariana")
        print("Tus ingredientes son: tomate, mozarella y salmón")

