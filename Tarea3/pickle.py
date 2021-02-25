#Tarea 3 en progreso...

try:
    import cPickle as pickle
except ImportError:
    import pickle

file = open('students.db', 'wb+')

students = ['python', 'monkey', 'camel']

pickle.dump(students, file, 2)