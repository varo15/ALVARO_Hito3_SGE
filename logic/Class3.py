def numerosRomanos():
    Vn = [100, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    Vc = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    NumeroRomano = []

    while (True):
        x = int(input("\n Ingresa un numero decimal / 0 terminar:"))

        if (x == 0):
            break

        i = 0

        while (x > 0):
            if (x >= Vn[i]):
                NumeroRomano.append(Vc[i])
                x = x - Vn[i]
            else:
                i = i + 1
        print(str(x), "=>", *NumeroRomano)


def main():
    numerosRomanos()
