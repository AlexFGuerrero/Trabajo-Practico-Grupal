a = -1
b = -1
tipo = -1

while not(tipo == 0 or tipo == 1 or tipo == 2):
    tipo = int(input("elija el tipo de operacion logica a realizar: \n 'OR' = 0   'AND' = 1  'NOT' = 2"))

while not(a == 0 or a == 1):
    a = int(input("Ingrese el valor 'A'(0/1): "))

if tipo != 2:
    while not(b == 0 or b == 1):
        b = int(input("Ingrese el valor 'B'(0/1): "))


if tipo == 0:
    resultado = a or b
    print(f"A or B = {int(resultado)}")
elif tipo == 1:
    resultado = a and b
    print(f"A and B = {int(resultado)}")
else:
    resultado = not(a)
    print(f"not(A) = {int(resultado)}")
