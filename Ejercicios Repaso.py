# Calculadora: introduce operacion y dos números para devolver la operacion resuelta.

operacion = input("¿Qué operación quieres realizar?: ")
primer_numero = int(input("Introduce el primer número: "))
segundo_numero = int(input("Introduce el segundo número: "))

if operacion == "+":
    resultado = primer_numero + segundo_numero
    print("El resultado es: {}".format(resultado))

elif operacion == "-":
    resultado = primer_numero - segundo_numero
    print("El resultado es: {}".format(resultado))

elif operacion == "*":
    resultado = primer_numero * segundo_numero
    print("El resultado es: {}".format(resultado))

else:
    resultado = primer_numero / segundo_numero
    print("El resultado es: {}".format(resultado))

# Adivina un número. Primero alguien introduce el número a adivinar para que, posteriormente, alguien intente adivinarlo.

numero_a_adivinar = int(input(" Introduce el número a adivinar: "))
intento = int(input("Adivina el número: "))

while numero_a_adivinar != intento:
    intento = int(input("Adivina el número: "))

print("!Has acertado¡ El número era {}".format(numero_a_adivinar))

# Transformar de grados Farenheit a grados centígrados. Sabiendo que (0 °C × 9/5) + 32 = 32 °F

grados_celsius = int(input("Introduce los grados Celsius: "))
grados_farenheit= (grados_celsius * 9/5)+ 32

print("{} grados celsius equivalen a {} grados farenheit".format(grados_celsius, grados_farenheit))