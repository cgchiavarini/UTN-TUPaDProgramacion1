nombre = input("Por favor ingrese su nombre: ")
opcion = int(input("Por favor seleccione una opcion (1 para mayusculas, 2 para minusculas, 3 para la primer letra en mayuscula): "))

mayusculas = nombre.upper()
minusculas = nombre.lower()
primera = nombre.title()


if opcion == 1:
    print("Su nombre es",mayusculas)
elif opcion == 2:
    print("Su nombre es",minusculas)
else:
    print("Su nombre es",primera)
