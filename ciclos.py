
continuar = True
contador = 0

# while continuar:
#     contador +=1
#     print(f'{contador}')
#
#     print('Deseas continuar:')
#     respuesta = input()
#
#     if respuesta == 's':
#         continue
#     else:
#         continuar = False


for i in range(1, 10, 2):
    print(f'Numero: {i + 1}')

    if i == 5:
        break

print('FIN')

