
def funcion(nombre='Juan', apellido='Valenzuela', lista=[]):
    print('Hello',nombre,apellido)
    print(f'lista: {lista}')
    lista[1]=9
    return lista

if __name__ == '__main__':
    lista=[1, 2, 3]
    l = funcion(lista=lista.copy())
    print(f'main: {lista}')
    print(l)
