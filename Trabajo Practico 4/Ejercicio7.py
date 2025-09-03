num = int(input("Por favor ingrese un numero entero positivo: "))
suma = 0

if 0 >= num:
    print("Debe ingresar un numero entero positivo")
else:
    for i in range(0,num+1):
        suma += i
    print(f"La suma de todos los numeros enteros comprendidos entre 0 y {num} es: {suma}")
