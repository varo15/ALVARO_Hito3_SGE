import statistics

def pedirNumeros():
    numero1 = int(input("Introduce numero 1: "))
    numero2 = int(input("Introduce numero 2: "))
    numero3 = int(input("Introduce numero 3: "))

    return numero1, numero2, numero3

def calcularMedia():


    num1, num2, num3 = pedirNumeros()
    numeros = [num1 , num2, num3]
    print("La media es: ", statistics.mean(numeros))
