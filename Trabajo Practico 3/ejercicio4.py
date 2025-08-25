edad = int(input("Por favor ingrese su edad: "))

if edad < 12:
    print ("Pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18:
    print ("Pertenece a la categoria Adolescente")
elif edad >= 18 and edad < 30:
    print ("Pertenece a la categoria Adulto/a joven")
else:
    print ("Pertenece a la categoria Adulto/a")
