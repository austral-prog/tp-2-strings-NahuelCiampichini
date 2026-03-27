def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """
    gasto = float(input("ingresar el gasto: "))
    dinero_recibido = int(input("Ingrese el dinero recibido: "))

    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    print("\nVuelto\n")
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    print("Pesos:")
    print(pesos)
    centavos = round((vuelto - pesos) * 100)
    print("Centavos:")
    print(centavos)
change()
