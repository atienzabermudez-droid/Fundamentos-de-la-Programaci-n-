RentaAnual = float(input("Introduce tu renta anual para decirte que impositivo te corresponde:"))

if RentaAnual < 10000 :
    print("Tu impositivo es del 5%")
elif RentaAnual >= 10000 and RentaAnual < 20000 :
    print("Tu impositivo es del 15%")
elif RentaAnual >= 20000 and RentaAnual < 35000 :
    print("Tu impositivo es del 20%")
elif RentaAnual >= 35000 and RentaAnual < 60000 :
    print("Tu impositivo es del 30%")
elif RentaAnual >= 60000 :
    print("Tu impositivo es del 45%")