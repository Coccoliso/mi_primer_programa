
operacion_a_realizar = input("¿Que operacion deseas realizar? (Suma / Resta / Multiplicacion / Division ").upper()



primer_numero = int(input("Indica el primer numero de la operacion: "))
segundo_numero = int(input("Indica el segundo numero de la operacion: "))
resultado_operacion = 0
if operacion_a_realizar == "SUMA":
    resultado_operacion = primer_numero + segundo_numero
elif operacion_a_realizar == "RESTA":
    resultado_operacion = primer_numero - segundo_numero
elif operacion_a_realizar == "MULTIPLICACION":
    resultado_operacion = primer_numero * segundo_numero
elif operacion_a_realizar == "DIVISION":
    resultado_operacion = primer_numero / segundo_numero

print("El resultado de la {} es de: {}".format(operacion_a_realizar, resultado_operacion))