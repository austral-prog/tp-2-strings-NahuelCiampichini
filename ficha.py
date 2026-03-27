def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    
    nombre_completo = input("Ingrese su nombre completo:")
    email = input("ingrese su email:")
    nota_1 = int(input("nota 1:"))
    nota_2 = int(input("nota 2:"))
    nota_3 = int(input("nota 3:"))
    nombre_completo_1 = nombre_completo.lstrip().rstrip().title()

    print("=" * 24)
    print("    FICHA DEL ALUMNO")
    print("=" * 24)
    print(f"Nombre: {nombre_completo_1.title()}")
    print(f"Email: {email.lower()}")
    print(f"Caracteres en nombre: {len(nombre_completo_1)}")
    print(f"Iniciales: {nombre_completo_1[0].upper()}{nombre_completo_1[nombre_completo_1.find(" ")+1].upper()}")
    print(f"Usuario: {nombre_completo_1[nombre_completo_1.find(" ")+1:].lower()}.{nombre_completo_1[0:nombre_completo_1.find(" ")].lower()}")
    print(f"Email valido: {"@" in email}")
    print(f"Dominio: {email[email.find("@")+1:].lower()}")
    print(f"Nombre para archivo: {nombre_completo_1.replace(" ", "_").title()}")
    print(f"Cantidad de a: {nombre_completo_1.count("a")}")
    print(f"Codigo secreto: {nombre_completo_1[::-1].upper()}")
    print(f"Nota 1: {nota_1}")
    print(f"Nota 2: {nota_2}")
    print(f"Nota 3: {nota_3}")
    print(f"Suma: {nota_1+nota_2+nota_3}")
    print(f"Promedio: {(nota_1+nota_2+nota_3)/3}")
    print(f"Promedio entero: {int((nota_1+nota_2+nota_3)/3)}")
    print("=" * 24)
ficha()
