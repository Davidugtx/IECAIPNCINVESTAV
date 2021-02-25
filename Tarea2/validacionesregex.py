import re

#email

def correo(texto1):

    # La validacion es muy debil, ingresar solo @ lo marca como valida
    # patron sencillo '[a-z.]+@([a-z.]+){1,2}[a-z]{2-3}'
    result=re.search("@",texto1)
    if result:
        print('Se encontro una arroba')
        validacion= 'Valido'
    else:
        print('No se encontro una arroba')
        validacion= 'No valido'
    return validacion

def numero_telefonico(texto2):

    # Solo cumple con el patron basico que se vio en clase
    # Patron para el tipo (331) 123-4567: '\([0-9]{3}\) [0-9]{3}-[0-9]{4}'
    patron = '[0-9]{10}'
    result = re.match(patron, texto2)
    if result:
        print('Numero ingresado correcto')
        validacion = 'Valido'
    else:
        print("Se debe de ingresar un numero valido")
        validacion = 'No valido'
    return validacion

def rfc(texto3):
    # La validacion es incorrecta, acepta una coma
    # el patron deberia ser => '[A-Z]{4}[0-9]{6}[A-Z0-9]{3}'
    patron = '[A-Z]{4}[0-9]{6}[A-Z,0-9]{3}'
    result = re.match(patron, texto3)
    if result:
        print('RFC ingresado correcto')
        validacion = 'Valido'
    else:
        print("Se debe de ingresar un RFC valido")
        validacion = 'No valido'
    return validacion

def curp(texto4):
    patron = '[A-Z]{4}[0-9]{6}[A-Z]{6}[0-9]{2}'
    result = re.match(patron, texto4)
    if result:
        print('CURP ingresado correcto')
        validacion = 'Valido'
    else:
        print("Se debe de ingresar un CURP valido")
        validacion = 'No valido'
    return validacion


if __name__ == '__main__':
    print('Funciones')
