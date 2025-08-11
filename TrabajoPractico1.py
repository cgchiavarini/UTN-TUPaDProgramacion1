#Ejercicio 1
print("Hola mundo!")

#Ejercicio2
nombre = input("Por favor ingresa tu nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Por favor ingresa tu nombre: ")
apellido = input("Por favor ingresa tu apellido: ")
edad = input("Por favor ingresa tu edad: ")
residencia = input("Por favor ingresa tu pais de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ejercicio 4
radio = int(input("Por favor ingrese el radio del círculo"))
area = 3.14 * radio ** 2
perimetro = 2 * 3.14 * radio
print(f"El área del círculo es {area}, y el perímetro es {perimetro}")

#Ejercicio 5
segundos = int(input("Por favor ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas} horas.")

#Ejercicio 6
numero = int(input("Por favor ingrese un numero: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

#Ejercicio 7
numero1 = int(input("Por favor ingrese un número entero distinto de 0: "))
numero2 = int(input("Por favor ingrese otro número entero distinto de 0: "))
print(f"La suma de {numero1} y {numero2} es {numero1 + numero2}")
print(f"La resta de {numero1} y {numero2} es {numero1 - numero2}")
print(f"La multiplicación de {numero1} y {numero2} es {numero1 * numero2}")
print(f"La división de {numero1} y {numero2} es {numero1 / numero2}")

#Ejercicio 8
altura = float(input("Por favor ingrese su altura: "))
peso = float(input("Por favor ingrese su peso: "))
print(f"Su IMC es {peso / (altura ** 2)}")

#Ejercicio 9
celsius = int(input("Por favor ingrese una temperatura en grados Celsius: "))
farenheit = (9/5 * celsius) + 32
print(f"El equivalente de {celsius} grados Celsius es {farenheit} grados Farenheit.")

#Ejercicio 10
numero1 = float(input("Por favor ingrese el primer número: "))
numero2 = float(input("Por favor ingrese el segundo número: "))
numero3 = float(input("Por favor ingrese el tercer número: "))
print(f"El promedio es {(numero1 + numero2 + numero3) / 3}")
