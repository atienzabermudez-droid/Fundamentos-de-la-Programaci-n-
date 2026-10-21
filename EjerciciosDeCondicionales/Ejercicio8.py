puntuacion = float(input("Introduce tu puntuación de evaluación:"))

if puntuacion == 0.0:
    dinero = puntuacion * 2400
    print("Tu nivel de rendimiento es: Inaceptable")
    print(f"Te corresponde una cantidad de dinero de: {dinero}€")

elif puntuacion == 0.4:
    dinero = puntuacion * 2400
    print("Tu nivel de rendimiento es: Aceptable")
    print(f"Te corresponde una cantidad de dinero de: {dinero}€")

elif puntuacion >= 0.6:
    dinero = puntuacion * 2400
    print("Tu nivel de rendimiento es: Meritorio")
    print(f"Te corresponde una cantidad de dinero de: {dinero}€")

else:
    print("Puntuación no válida. Debe ser 0.0, 0.4 o 0.6 en adelante.")