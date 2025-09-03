suma = 0
cont = 0

for i in range(0,100):
    num=int(input("Por favor ingrese un numero entero: "))
    cont += 1
    suma += num
print(f"La media de los valores ingresados es {suma / cont}.")
