# def funcion():
#     pass       #funcion, no hace nada pero se puede llamar desde cualquier parte
#
# if __name__ == '__main__':
#     funcion()

# def funcion():
#     print('Hello')     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
# if __name__ == '__main__':
#     funcion()

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
# if __name__ == '__main__':
#     funcion('David')

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return 'ok'
#
# if __name__ == '__main__':
#     ret = funcion('David')
#
#     print(ret)

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return
#
# if __name__ == '__main__':
#     ret = funcion('David')
#
#     print(ret)

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return [1, 2, 3]
#
# if __name__ == '__main__':
#     ret = funcion('David')
#
#     print(ret)

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return [1, 2, 3]
#
# if __name__ == '__main__':
#     ret, re2, r3= funcion('David')
#
#     print(ret)

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return (1, 2, 3)
#
# if __name__ == '__main__':
#     ret, re2, r3= funcion('David')
#
#     print(ret)

# def funcion(nombre):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return ({1: 'uno'}, [2], (3,))
#
# if __name__ == '__main__':
#     ret, re2, r3= funcion('David')
#
#     print(ret)

# def funcion(nombre='David'):
#     print('Hello', nombre)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return ({1: 'uno'}, [2], (3,))
#
# if __name__ == '__main__':
#     ret, re2, r3= funcion()
#
#     print(ret)

# def funcion(nombre='David', apellido= 'Ortega'):
#     print('Hello', nombre, apellido)     #funcion, no hace nada pero se puede llamar desde cualquier parte
#
#     return ({1: 'uno'}, [2], (3,))
#
# if __name__ == '__main__':
#     ret, r2, r3= funcion()
#
#     print(ret)

# def funcion(nombre='David', apellido= 'Ortega', lista=[]):
#     print('Hello', nombre, apellido)
#     print(f'lista: {lista}')
#
#     return lista
#
# if __name__ == '__main__':
#     l = funcion()
#
#     print(l)

# def funcion(nombre='David', apellido= 'Ortega', lista=[]):
#     print('Hello', nombre, apellido)
#     print(f'lista: {lista}')
#
#     return lista
#
# if __name__ == '__main__':
#     lista = [1, 2, 3]
#     l = funcion(lista=lista)
#
#     print(l)

# def funcion(nombre='David', apellido= 'Ortega', lista=[]):
#     print('Hello', nombre, apellido)
#     print(f'lista: {lista}')
#
#     lista[1] = 9
#
#     return lista
#
# if __name__ == '__main__':
#     lista = [1, 2, 3]
#     l = funcion(lista=lista)
#
#     print(l)


# def funcion(nombre='David', apellido= 'Ortega', lista=[]):
#     print('Hello', nombre, apellido)
#     print(f'funcion: {lista}')
#
#     lista[1] = 9
#
#     return lista
#
# if __name__ == '__main__':
#     lista = [1, 2, 3]
#     l = funcion(lista=lista)
#
#     print(f'main: {lista}')
#     print(l)


def funcion(nombre='David', apellido= 'Ortega', lista=[]):
    print('Hello', nombre, apellido)
    print(f'funcion: {lista}')

    lista[1] = 9

    return lista

if __name__ == '__main__':
    lista = [1, 2, 3]
    l = funcion(lista=lista.copy())

    print(f'main: {lista}')
    print(l)

# def funcion(nombre='David', apellido='Ortega', lista=['a','9','c']):
#     print('Hello', nombre, apellido)
#
#
#     lista[1]=9
#     print(
#     return lista
#
#
# if __name__ == '__main__': _______))))___++++
#     lista = [1, 2, 3]
#
#     l = funcion(lista=lista)
#
#     print(ret)
#
#
# def funcion(nombre='Juan'):
#     print('Hello', nombre)
#
#     return ({1: 'uno'}, [2], (3,))
#
#
# if __name__ == '__main__':
#     ret, r2, r3 = funcion()
#
#     print(ret)