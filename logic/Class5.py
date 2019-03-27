from time import sleep


def crearLista():
    lista = []

    while (len(lista) <= 4):
        numero = int(input("Introduce numero positivo:"))
        if (numero >= 0):
            lista.append(numero)
    return lista


def comprobarNumeroLista(lista):
    lista = lista
    numero = int(input("Introduce numero a comprobar:"))
    print("Si el numero", numero, "se encuentra en la lista, se pondra un 0 en las posiciones que ocupe\n")
    sleep(1)
    for i in range(len(lista)):
        if numero == lista[i]:
            lista[i] = 0
    return lista


def main():
    print(comprobarNumeroLista(crearLista()))
