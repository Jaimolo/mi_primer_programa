
b = input("Introduce un número: ")

numeros = []
numeros.append(b)
while b != "FIN":
    b = input("Dame un número: ")
    numeros.append(b)

pequeño = numeros[0]

for i in numeros:
    if i < pequeño:
        i = pequeño

print("El número más pequeño es el {}".format(pequeño))

