while (True):
    arabi = int(input('Ingresa un número arábigo: '))
    if arabi>0 and arabi<31:
        x=(arabi//10)*'X'
        xs = arabi%10
        vs = xs%5
        if xs == 9:
            i = 'IX'
            print(x+i)
        elif vs == 4:
            i = 'IV'
            print(x+i)
        else:
            i = vs*'I'
            v=(xs//5)*'V'
            print(x+v+i)
    else:
        print('No podemos operar esos números')