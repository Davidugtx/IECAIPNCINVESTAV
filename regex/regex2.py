import re


def suma(a, b):
    patron = '[0-9]*$'

    ra = re.match(patron, str(a))
    rb = re.match(patron, str(b))

    if ra and rb:
        return int(a) + int(b)
    else:
        print('Se deben ingresar numeros positivos')


if __name__ == '__main__':
    print(suma(2, 3))