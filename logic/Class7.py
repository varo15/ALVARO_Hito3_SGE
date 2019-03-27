import string


def main():
    text = str(input("Introduce texto:"))
    listaTexto = list(text)
    for i in range(len(listaTexto)):
        x = int(string.ascii_letters.index(listaTexto[i]) + 1)
        print(listaTexto[i], "= ", x)
