# crear lista
lista = ['hola', 2, 3.4, False, (1, 'test'), 2, 'Hello', 2]
lista2 = list()

print(f'lista: {lista}')
lista[4] = [2, 'test2']
print(f'lista: {lista}')

# print(f'lista2: {lista2}')
# print(type(lista))

# agregar elementos
#    append()
lista.append('Pedro')
print(f'lista: {lista}')

#    insert()
lista.insert(3, True)
print(f'lista: {lista}')


# eliminar elementos
#    eliminar elemento
print(f'lista: {lista}')

#    obtener elemento y eliminarlo
l = lista.pop(4)
print(f' --> lista: {lista}')
print(f'l: {l}')

# obtener indice de un objeto
indice = lista.index(True)
print(f'indice: {indice}')

# contar elementos
conteo = lista.count(2)
print(f'conteo: {conteo}')

# ordenar}
lista2 = [4, 6, 2, 7, 3, 5]
lista2.sort()
print(f'lista: {lista2}')

# orden inverso
lista2.reverse()
print(f'lista: {lista2}')

# extender lista
print(f'lista: {lista}')
print(f'lista2: {lista2}')

lista.extend(lista2)
print(f'lista: {lista}')

# copiar
l1 = lista2
l2 = l1.copy()

print(f'l1: {l1}')
print(f'l2: {l2}')

l2[2] = 10
print(f'l2: {l2}')
print(f'l1: {l1}')
print(f'lista2: {lista2}')

# operador slice
print('\n\nOperador slice')
print(f'lista2: {lista}')
sublista = lista[4:9]
print(f'sublista: {sublista}')


sublista = lista[-3:-6:-2]
print(f'sublista: {sublista}')

reverse_lista = lista[::-1]
print(f'reverse_lista: {reverse_lista}')

l3 = [1, 2, 3]
l4 = l3[:]

print(l3)
print(l4)

l4[1] = 5
print(l3)
print(l4)