def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio = int(input("Precio: "))
    descuento = float(input("Descuento: "))
    cantidad = int(input("Cantidad: "))
    precio_descuento = precio - descuento
    total = precio_descuento * cantidad


    print("Precio:", precio)
    print("Descuento:", descuento)
    print("Precio con descuento:", precio_descuento)
    print("Total:", total)
#casting()

