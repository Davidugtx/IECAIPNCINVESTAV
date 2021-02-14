# #crear lista
# lista = ['hola', 2, 3.4, False, (1, 'test'), 2, 'Hello', 2]
# lista2 = list()

#print(lista[4][1])
# print(f'lista: {lista}')
# lista[4] = [2, 'test2']
# print(f'lista: {lista}')
# print(f'lista2: {lista2}')
#
# print(type(lista))

#crear tupla
# tupla = ('hola', 2, 3.4, False, [1, 'test'], 2, 'Hello', 2)
#elemento1, tupla  = 'hola', (2, 3.4, False, [1, 'test'], 2, 'Hello', 2)  #asignacion multipe
#elemento1, tupla  = ('hola', 6), (2, 3.4, False, [1, 'test'], 2, 'Hello', 2)  #asignacion multipe
#elemento1, tupla, e1, e2, e3, e4, e5, e6  = 'hola', 2, 3.4, False, [1, 'test'], 2, 'Hello', 2
#_, _, _, _, e3, _, e5, e6  = 'hola', 2, 3.4, False, [1, 'test'], 2, 'Hello', 2
#e, e, e, e, e, e, e, e  = 'hola', 2, 3.4, False, [1, 'test'], 2, 'Hello', 2  #valor de e ultimo valor de la tupla
# tupla = ('hola',)
# #tupla = 'hola',
# tupla2 = tuple()

#print(f'elemento1: {elemento1}')
# print(f'e3: {e3}')
# print(f'e5: {e5}')
# print(f'e6: {e6}')

# tupla = 'hola', 2, 3.4, False, [1, 'test'], 2, 'Hello', 2
# print(tupla[-8])
# print(tupla[0])


pass
# print(f'tipo: {type(tupla)}')

# print(f'tupla: {tupla[0]}')
# print(f'tupla: {tupla[1]}')
# print(f'tupla: {tupla[2]}')
# print(f'tupla: {tupla[3]}')
# print(f'tupla: {tupla[4][1]}')
# print(f'tupla2: {tupla2}')
#
# print(type(tupla))

# tupla[1] = 3

# conteo = tupla.count('hol')
# print(f'conteo: {conteo}')

# index = tupla.index(2,6)
# print(f'indice: {index}')

# #operador slice lista
#
# lista = ['hola', 2, 3.4, True, [2, 'test2'], 2, 'Hello', 2, 'Pedro', 7, 6, 5, 4, 3, 2]
# print('Operador slice')
# print(f'lista: {lista}')
# print(f'lista: {lista[4:9]}')
#
# reverse_lista = lista[::-1]
# print(f'reverse:lista: {reverse_lista}')

# #operador slice tupla
#
# tupla = ('hola', 2, 3.4, True, [2, 'test2'], 2, 'Hello', 2)
# print('\n\nOperador slice tupla')
# print(f'tupla: {tupla}')
# subtupla = tupla[4:8]
# print(f'subtupla: {subtupla}')
#
# lista = list(tupla)
# print(lista)
#
# tup = tuple(lista[3:6])
# print(tup)

a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(f'slice: {a[-5:-1]}')
print(f'slice: {a[:-1]}')
print(f'slice: {a[-5:]}')