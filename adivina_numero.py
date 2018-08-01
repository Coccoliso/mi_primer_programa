


number_to_guess = 2

user_number = int(input('Adivina un numero: '))

if number_to_guess == user_number:
    print('Has ganado')
else:
    user_number = int(input('Introduzca otro numero: '))
    if number_to_guess == user_number:
        print('Has ganado')
    else:
        user_number = int(input('Introduzca otro numero: '))
        if number_to_guess == user_number:
            print('Has ganado')
        else:
            user_number = int(input('Introduzca otro numero: '))
            if number_to_guess == user_number:
                print('Has ganado')
            else:
                user_number = int(input('Introduzca otro numero: '))
                if number_to_guess == user_number:
                    print('Has ganado')
                else:
                    print('Has perdido')