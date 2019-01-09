

texto = input("Introduce una frase: ")

vocales = []
resto = []

for i in texto:
    if i == "a" or i== "e" or i=="i" or i=="o" or i=="u":
        vocales.append(i)
    else:
        resto.append(i)

print(vocales)