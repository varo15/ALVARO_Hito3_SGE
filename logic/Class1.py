""" Funcion que calcula los numeros pares entre un rango de numeros  los imprime por pantalla"""


def encontrarPares(num1, num2):
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i, "=> Numero par")


"""Comprobamos que los numeros sean postivos"""


def pedirNumeros():
    numerosCorrectos = False
    while numerosCorrectos == False:

        numero1 = int(input("Introduce un numero entero positivo: "))
        numero2 = int(input("Introduce otro numero entero positivo: "))

        if numero1 >= 0 & numero2 >= 0:
            numerosCorrectos = True

    return numero1, numero2


"""Funcion principal"""


def numeroPares():
    print("Numeros Pares\n")
    numero1, numero2 = pedirNumeros()

    if numero2 < numero1:
        numero1, numero2 = numero2, numero1
        encontrarPares(numero1, numero2)
    else:
        encontrarPares(numero1, numero2)

