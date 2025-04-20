a = 0
b = 0
tipo = 0

while True:
    # Solicitar datos de entrada
    tipo = int(
        input(
            "Elija el tipo de operacion logica a realizar:\n \t1. OR\n   \t2. AND\n  \t3. NOT\n \t4. Salir \n\tElección: "
        )
    )
    # comprobar que todos los datos estén ingresados
    if tipo == 4:
        print("Saliendo...")
        break
    elif tipo not in [1, 2, 3]:
        print("Ingrese una opción correcta")
        continue
    elif tipo == 1:
        a = int(input("Ingrese el valor 'A'(0/1): "))
        b = int(input("Ingrese el valor 'B'(0/1): "))
        while a not in [0, 1] or b not in [0, 1]:
            print("A o B deben ser 0 o 1")
            a = int(input("Ingrese nuevamente un valor para 'A'(0/1): "))
            b = int(input("Ingrese nuevamente un valor para 'B'(0/1): "))
        
    elif tipo == 2:
        a = int(input("Ingrese el valor 'A'(0/1): "))
        b = int(input("Ingrese el valor 'B'(0/1): "))
        while a not in [0, 1] or b not in [0, 1]:
            print("A o B deben ser 0 o 1")
            a = int(input("Ingrese nuevamente un valor para 'A'(0/1): "))
            b = int(input("Ingrese nuevamente un valor para 'B'(0/1): "))
        
    elif tipo == 3:
        a = int(input("Ingrese un valor (0/1): "))
        while a not in [0, 1] or b not in [0, 1]:
            print("A o B deben ser 0 o 1")
            a = int(input("Ingrese nuevamente un valor para 'A'(0/1): "))

    # Realizar las tablas
    if tipo == 1:
        resultado = a or b
        print(f"A or B = {resultado}")
    elif tipo == 2:
        resultado = a and b
        print(f"A and B = {resultado}")
    elif tipo == 3:
        not_a = not (a)
        print(f"not A = {not_a}")