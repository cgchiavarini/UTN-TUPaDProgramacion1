num1 = int(input("Por favor ingrese el primer numero: "))
num2 = int(input("Por favor ingrese el segundo numero: "))
suma = 0

if num1 >= num2:
    print("El primer numero deberia ser menor que el segundo.")
else:
    for i in range(num1+1,num2):
        suma += i
    print(f"La suma de todos los numeros enteros comprendidos entre {num1} y {num2} es: {suma}")
