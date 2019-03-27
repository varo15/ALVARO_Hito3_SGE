def crearLista():
    lista = []

    for i in range(0, 3):
        numero = int(input("Introduce un numero entero: "))
        lista.append(numero)
    return lista


def tratamientoListas():
    print("Primera lista:\n")
    lista1 = crearLista()
    print("Segunda lista:\n")
    lista2 = crearLista()

    lista1.extend(lista2)
    lista1.sort(reverse=True)

    return lista1


def main():
    # Definimos las listas finales
    listaMultiplos = []
    listaFinal = []

    # Llamamos al metodo que crea y concatena las 2 listas
    lista = tratamientoListas()

    # Quitamos los multiplos de 5 de la lista

    for i in range(0, len(lista)):
        # Si el elemento i de la lista es divisible entre 5, lo añadimos a la lista 'listaMultiplos'
        if (lista[i] % 5 == 0):
            listaMultiplos.append(lista[i])
        # Si el elemento i de a lista no es divisible entre 5, lo añadimos a la lista 'listaFinal'
        else:
            listaFinal.append(lista[i])

    print("Lista final: ", listaFinal)
    print("Lista multiplos de 5:", listaMultiplos)
