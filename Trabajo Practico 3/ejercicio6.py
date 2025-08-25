from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
moda =mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Hay Sesgo Positivo.")
elif media < mediana and mediana < moda:
    print ("Hay Sesgo Negativo")
else:
    print("Sin Sesgo")
