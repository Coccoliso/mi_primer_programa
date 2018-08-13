
texto_usuario = input("Introduzca un texto: ")

mayuscula = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Y", "X", "Z"]


n_mayuscula = 0

for letra in texto_usuario:
    if letra in mayuscula:
        n_mayuscula += 1

print("El numero de letras mayusculas es de {}.".format(n_mayuscula))