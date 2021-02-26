try:
    import cPickle as pickle
except ImportError:
    import pickle


file = open('data.dat', 'wb+')

animals = ['python', 'monkey', 'camel']

bin_animal = pickle.dumps(animals)
print(bin_animal)

pickle.dump(animals, file, 1)

file.seek(0)
unpickler = pickle.Unpickler(file)

print(unpickler)
read_animal = unpickler.load()

print(read_animal)


file.close()
with open('data.dat', 'wb+') as file:
    pass

print(file.closed)





