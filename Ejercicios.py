
texto_usuario = input("Introduce una frase: ")

n_mayus = 0
n_minus = 0

for i in texto_usuario:
    if i >= "A" and i <="Z":
        n_mayus +=1
    else:
        n_minus +=1

print(n_mayus)




#Crea un programa que muestre todas las vocales que aparecen en la string#

texto = input("Introduce una frase: ")

vocales = []
resto = []

for i in texto:
    if i == "a", "e", "i", "o" or "u":
        vocales.append(i)
    else:
        resto.append(i)

print(vocales)

