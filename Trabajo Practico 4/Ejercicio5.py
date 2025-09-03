import random
print("Vamos a jugar a adivinar un numero.")
num = int(input("Ingrese un numero del 0 al 9: "))
objetivo = random.randint(0,9)
cont = 0

if num > 9 or num < 0:
    print("Debe ingresar un numero del 0 al 9.")
else:
    while num != objetivo:
        cont += 1
        num = int(input("Incorrecto. Prueba de nuevo: "))
    print(f"Correcto! El numero a adivinar era {num}, y le llevo {cont} intentos adivinarlo.")
