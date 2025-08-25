palabra = input("Por favor ingrese una frase o palabra: ").lower()

ultimo_caracter = palabra[-1]

if (ultimo_caracter == 'a' or ultimo_caracter == 'e' or ultimo_caracter == 'i' or
    ultimo_caracter == 'o' or ultimo_caracter == 'u'):
    print(palabra + "!")
else:
    print(palabra)
