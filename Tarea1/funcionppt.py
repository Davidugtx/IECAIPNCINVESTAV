def juego():
        while True:
            print('Bienvenido al juego de piedra, papel o tijera')
            print('\t1) piedra')
            print('\t2) papel')
            print('\t3) tijera')

            seleccion = int(input('Ingresa tu seleccion en este espacio: '))
            from random import randint

            numero = randint(0, 2)

            opciones = ['piedra', 'papel', 'tijera']




            usuario= opciones[seleccion - 1]

            seleccion_pc = opciones[numero-1]

            print(f'Usuario: {usuario} vs {seleccion_pc} :PC')

            if usuario != seleccion_pc :
                if usuario == 'piedra' and  seleccion_pc == 'papel':
                    print('Perdiste!')
                if usuario == 'papel' and seleccion_pc == 'tijera':
                    print('Perdiste!')
                if usuario == 'tijera' and seleccion_pc == 'piedra':
                    print('Perdiste!')
                if usuario == 'piedra' and  seleccion_pc == 'tijera':
                    print('Ganaste!')
                if usuario == 'tijera' and seleccion_pc == 'papel':
                    print('Ganaste!')
                if usuario == 'papel' and seleccion_pc == 'piedra':
                    print('Ganaste!')

            else:
                print('Empate')




            turno=int(input('¿Deseas volver a jugar otra vez?: (1 Si) (2 No)?: '))
            if turno !=1:
               break
        print("Hasta luego")
        return None

if __name__ == '__main__':
    print(juego())
    #finalizado