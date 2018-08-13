

texto_usuario = input("Introduce una frase: ")

espacio = " "
coma = ","
punto = "."

n_espacios = 0
n_comas = 0
n_puntos = 0

for letra in texto_usuario:
    if letra in espacio:
        n_espacios += 1
    elif letra in coma:
        n_comas += 1
    elif letra in punto:
        n_puntos += 1

print("El numero de espacios es de {}.".format(n_espacios))
print("El numero de comas es de {}.".format(n_comas))
print("El numero de puntos es de {}.".format(n_puntos))