pares= 0
impares = 0
positivos = 0
negativos = 0

for i in range(0,100):
    num = int(input("Por favor ingrese un numero entero: "))
    if num % 2 == 0:
        pares +=1
    else:
        impares +=1
    if num > 0:
        positivos +=1
    else:
        negativos +=1

print(f"Numeros pares: {pares}. Numeros impares: {impares}. Numeros positivos: {positivos}. Numeros negativos: {negativos}.")
