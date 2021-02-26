
import shelve

class animal:
    nombre = ''
    familia = ''

with shelve.open('prueba_shelve') as objeto_shelve:
    for os in objeto_shelve:
        print(f'{os}: {objeto_shelve[os]}')