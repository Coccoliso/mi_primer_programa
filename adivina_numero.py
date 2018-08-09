


number_to_guess = int(input("Jugador 1: indica el numero a adivinar: "))

user_number = int(input('Jugador 2: adivina el numero: '))

while number_to_guess != user_number:
    if number_to_guess == user_number:
        print('Has ganado')
    else:
        user_number = int(input('Introduzca otro numero: '))

print("Juego terminado")