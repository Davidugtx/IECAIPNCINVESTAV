try:
    import cPickle as pickle
except ImportError:
    import pickle

#e = []


class estudiante:
    nua = ''
    nombre = ''
    correo = ''
    contrasena = ''
    def __init__(self, nua='', nombre='', correo='', contrasena=''):
        self.nua = nua
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena

    def __repr__(self):
        return str(self.__dict__)

    def setnua(self, nua):
        self.nua = nua


    def getnua(self):
        return self.nua


    def setNombre(self, nombre):
        self.nombre = nombre


    def getNombre(self):
        return self.nombre


    def setcorreo(self, correo):
        self.correo = correo


    def getcorreo(self):
        return self.correo


    def setcontrasena(self, contrasena):
        self.contrasena = contrasena


    def getcontrasena(self):
        return self.contrasena


def guardar():
    nua = input('Ingrese el numero unico de alumno (nua): ')
    nombre = input('Ingrese el nombre: ')
    correo = input('Ingrese el correo: ')
    contrasena = input('Ingrese la contrasena: ')
    ObjetoE = estudiante(nua, nombre, correo, contrasena)
    e.append(ObjetoE)
    file = open('students.db', 'wb+')
    pickle.dump(f'NUA= {ObjetoE.nua}', file)
    pickle.dump(f'Nombre= {ObjetoE.nombre}', file)
    pickle.dump(f'Correo= {ObjetoE.correo}', file)
    pickle.dump(f'Contrasena= {ObjetoE.contrasena}', file)
    file.close()
    print(f'Archivo cerrado: {file.closed} ')
    print('Alumno guardado')


def leer():
    file = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file)
    read_alumno=unpickler.load()
    print(read_alumno)
    print(f' e:\n {e}')
    print('Alumnos mostrados')

def actualizar():
    nua=input('Ingrese el numero unico de alumno (nua): ')
   # if nua != ObjetoE.nua
    #    print('Error\n')
   # else:
    nombre = input('Modifique el nombre: ')
    setnombre(nombre)
    correo = input('Modifique el correo: ')
    setcorreo(correo)
    contrasena = input('Modifique la contrasena: ')
    setcontrasena(contrasena)
    print('Datos del estudiante actualizado')



if __name__ == '__main__':

    while True:
        print('-----Menu-----')
        print('1- Guardar estudiante\n2- Leer estudiante \n3- Actualizar estudiante')
        sel= int(input('Escoja una opcion escribiendo su numero aqui: '))
        if sel== 1:
            guardar()
        elif sel== 2:
            leer()
        elif sel== 3:
            actualizar()
        else:
            print("ERROR")
