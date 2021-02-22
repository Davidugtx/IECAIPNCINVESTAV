from validacionesregex import correo
from validacionesregex import numero_telefonico
from validacionesregex import curp
from validacionesregex import rfc


def main():
    print('Iniciando programa')
    print('Por favor ingrese su correo electronico: ', end='')
    texto1 = input()
    print(f'Correo ingresado:  {texto1}')
    r1=correo(texto1)
    print(r1)
    print('Por favor ingrese su numero telefonico: ', end='')
    texto2 = input()
    print(f'Numero telefonico ingresado:  {texto2}')
    r2=numero_telefonico(texto2)
    print(r2)
    print('Por favor ingrese su RFC: ', end='')
    texto3 = input()
    print(f'RFC ingresado:  {texto3}')
    r3 = rfc(texto3)
    print(r3)
    print('Por favor ingrese su CURP: ', end='')
    texto4 = input()
    print(f'CURP ingresado:  {texto4}')
    r4 = curp(texto4)
    # print(r2)
    print(r4)

if __name__ == '__main__':
    main()
