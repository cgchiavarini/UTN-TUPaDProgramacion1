hemisferio = input("¿En qué hemisferio se encuentra? (Norte/Sur): ").lower()
mes = input("¿Qué mes es? (Enero, Febrero, etc): ").lower()
dia = int(input("¿Qué día es? (1-31): "))

if hemisferio == "norte":
    if (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 20):
        estacion = "primavera"
    elif (mes == "junio" and dia >= 21) or (mes == "julio") or (mes == "agosto") or (mes == "septiembre" and dia <= 22):
        estacion = "verano"
    elif (mes == "septiembre" and dia >= 23) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        estacion = "otoño"
    else:
        estacion = "invierno"
elif hemisferio == "sur":
    if (mes == "septiembre" and dia >= 23) or (mes == "octubre") or (mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        estacion = "primavera"
    elif (mes == "diciembre" and dia >= 21) or (mes == "enero") or (mes == "febrero") or (mes == "marzo" and dia <= 20):
        estacion = "verano"
    elif (mes == "marzo" and dia >= 21) or (mes == "abril") or (mes == "mayo") or (mes == "junio" and dia <= 22):
        estacion = "otoño"
    else:
        estacion = "invierno"
else:
    estacion = "Hemisferio no válido"

print(f"El usuario se encuentra en {estacion}.")
