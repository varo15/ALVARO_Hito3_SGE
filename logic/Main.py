from time import sleep

from logic import Class1, Class2, Class4, Class5, Class7

def main():
    print("---------- M E N U ----------")
    print("1- Ejercicio 1")
    print("2- Ejercicio 2")
    print("3- Ejercicio 3")
    print("4- Ejercicio 4")
    print("5- Ejercicio 5")
    print("6- Ejercicio 6")
    print("7- Ejercicio 7")
    print("8- Ejercicio 8")
    print("9- Salir")

    option = int(input("Introduce opcion"))

    if option == 1:
        Class1.numeroPares()
    elif option == 2:
        Class2.calcularMedia()
    elif option == 3:
        print("No disponible")
    elif option == 4:
        Class4.main()
    elif option == 5:
        Class5.main()
    elif option == 6:
        print("No disponible")
    elif option == 7:
        Class7.main()
    elif option == 8:
        print("En progres")
    elif option == 9:
        print("Cerrando el programa...")
        sleep(0.5)

main()