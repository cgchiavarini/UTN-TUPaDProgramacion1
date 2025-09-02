CORTE = 0
suma= 0
num = int(input("Por favor ingrese un numero entero: "))
while num != CORTE:
    suma += num
    num = int(input("Por favor ingrese otro numero entero: "))
print(f"La suma de todos los numeros ingresados es: {suma}.")
