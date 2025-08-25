magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("El terremoto ha sido muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("El terremoto ha sido leve")
elif magnitud >=4 and magnitud < 5:
    print("El terremoo ha sido moderado")
elif magnitud >=5 and magnitud < 6:
    print("El terremoo ha sido fuerte")
elif magnitud >=6 and magnitud < 7:
    print("El terremoo ha sido muy fuerte")
else:
    print("El terremoto ha sido extremo")
