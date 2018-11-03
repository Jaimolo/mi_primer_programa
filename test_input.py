

number_to_guess = 2

user_number = int(input(" Adivina un número: "))

while number_to_guess != user_number:
    print("Has fallado")
    user_number = int(input("Introduce otro número: "))
print(" Has acertado")
