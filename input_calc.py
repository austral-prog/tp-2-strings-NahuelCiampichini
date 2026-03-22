def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = float(input("Base: "))
    altura = float(input("Altura: "))
    area = int(base) * int(altura)
    perimetro = 2 * int(base) + 2 * int(altura)

    print(f"Base: {int(base)}\nAltura: {int(altura)}\nArea: {area}\nPerimetro: {perimetro}")

