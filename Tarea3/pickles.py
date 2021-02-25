#Tarea 3 en progreso...

try:
    import cPickle as pickld
except ImportError:
    import pickle

file = open('students.db', 'wb+')

students = ['python', 'monkey', 'camel']

pickle.dump(students, file, 2)

ab = pickle.dumps(students)
print(f' ab: {ab}')
print(f'type(ab): {type(ab)}')