
import shelve

class animal:
    nombre  = ''
    familia = ''

objeto_animal = animal()

animals = ('python', 'monkey', 'camel')

with shelve.open('prueba_shelve') as objeto_shelve:
    objeto_shelve['animals'] = animals

    objeto_shelve['entero'] = 15
    objeto_shelve['decimal'] = 3.4

    objeto_shelve['clase'] = animal

    objeto_shelve['objeto']= objeto_animal