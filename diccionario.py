diccionario = {}
#diccionario2 = dict()

print(f'diccionario: {diccionario}')
print(f'tipo: {type(diccionario)}')

diccionario[1] = 'uno'
diccionario[3.4] = 'tres punto cuatro'
diccionario['uno'] = 'uno'
diccionario[False] = 'Falso'

print(f'diccionario[1]: {diccionario[1]}')
print(f'diccionario[3.4]: {diccionario[3.4]}')
print(f'diccionario["uno"]: {diccionario["uno"]}')
print(f'diccionario[False]: {diccionario[False]}')

print(f'diccionario: {diccionario}')


diccionario2 = {1: 'uno', 2.0: 'dos punto cero'}
print(diccionario2)

# ret = diccionario.pop(3.4)
# print(ret)
# print(diccionario)
#
print('\n\n')
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())


for key in diccionario.keys():
    print(f'key: {key}')
    print(f'valor: {diccionario[key]}')
    print()