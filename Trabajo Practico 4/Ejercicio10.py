numero_invertido = 0
digito = 0
num = int(input("Por favor ingrese un numero entero: "))

while num > 0:
     digito = num % 10
     numero_invertido = numero_invertido * 10 + digito
     num = num // 10

print(f"El numero invertido es {numero_invertido}.")
