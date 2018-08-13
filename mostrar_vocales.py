
texto_usuario = input("Introduzca un texto: ").upper()

vocal_a = "A"
vocal_e = "E"
vocal_i = "I"
vocal_o = "O"
vocal_u = "U"

vocales = []


for letra in texto_usuario:
    if letra in vocal_a:
        vocales.append(vocal_a)
    elif letra in vocal_e:
        vocales.append(vocal_e)
    elif letra in vocal_i:
        vocales.append(vocal_i)
    elif letra in vocal_o:
        vocales.append(vocal_o)
    elif letra in vocal_u:
        vocales.append(vocal_u)



print("La vocales de nuestro texto son: {}.".format(vocales))
