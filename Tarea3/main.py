import os
from os import remove
try:
    import cPickle as pickle
except ImportError:
    import pickle




class estudiante:
    number_of_students=0
    nua = ''
    nombre = ''
    correo = ''
    contrasena = ''
    def __init__(self, nua='', nombre='', correo='', contrasena=''):
        self.nua = nua
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        estudiante.number_of_students +=1


# How to Count the Number of Objects in a Class in Python
# link: http://www.learningaboutelectronics.com/Articles/How-to-count-the-number-of-objects-in-a-class-in-Python.php



def guardar():
    nua_inicial = input('Ingrese el numero unico de alumno (NUA): ')
    file = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file)
    v = estudiante.number_of_students
    for i in range(v):
        read_alumno = unpickler.load()
        if nua_inicial == read_alumno.nua:
            print('NUA ya registrado, por favor vuelva a escoger la opcion 1-Guardar estudiante  del Menu e ingrese otro NUA diferente')
            switch()
        else:
            continue
    nua = nua_inicial
    nombre = input('Ingrese el nombre: ')
    correo = input('Ingrese el correo: ')
    contrasena = input('Ingrese la contrasena: ')
    ObjetoE= estudiante(nua, nombre, correo, contrasena)
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    file.close()
    print(f'Archivo cerrado: {file.closed} ')
    print('El numero de estudiantes en la clase es: ' + str(estudiante.number_of_students))
    print('Alumno guardado')




def leer():
    file = open('students.db', 'rb')

    unpickler = pickle.Unpickler(file)
    v=estudiante.number_of_students
    for i in range(v):
        read_alumno=unpickler.load()
        print(f' NUA: {read_alumno.nua}')
        print(f' Nombre: {read_alumno.nombre}')
        print(f' Correo: {read_alumno.correo}')
        print(f' Contrasena: {read_alumno.contrasena}')

    print('Alumnos mostrados')

def actualizar():
    nua_inicial = input('Ingrese el numero unico de alumno (NUA): ')
    file = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file)
    v = estudiante.number_of_students
    j=0
    for i in range(v):
        read_alumno = unpickler.load()
        j=j+1
        if nua_inicial == read_alumno.nua:
            break
        elif j==v:
            print('NUA no encontrado, por favor vuelva a escoger la opcion 3-Acutalizar estudiante del Menu e ingresa un NUA valido')
            switch()
        else:
            continue
    read_alumno.nua = nua_inicial
    read_alumno.nombre = input('Ingrese el nombre: ')
    read_alumno.correo = input('Ingrese el correo: ')
    read_alumno.contrasena = input('Ingrese la contrasena: ')
    actualizacion=estudiante(read_alumno.nua,read_alumno.nombre,read_alumno.correo,read_alumno.contrasena)
    print('Alumno guardado')


def crearguardar5objest():    #crear 5 objetos de estudiante y guardarlos en students.db
    ObjetoE1 = estudiante('703270', 'David Fernando Ortega Tamayo', 'df.ortegatamayo@ugto.mx', '123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE1, file)
    ObjetoE2 = estudiante('703271', 'Jose Amparo Andrade Lucio', 'andrade@ugto.mx', 'wadaw22')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE2, file)
    ObjetoE3 = estudiante('703272', 'Roberto Rojas Laguna', 'rr.rojaslaguna@ugto.mx', '1d2d23456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE3, file)
    ObjetoE4 = estudiante('703273', 'Oscar Ibarra Almanza', 'oscar@ugto.mx', '33d123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE4, file)
    ObjetoE5 = estudiante('703274', 'Estudillo Ayala Ramirez', 'estudillo@ugto.mx', '1dd223456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE5, file)
    file.close()
    print('Creacion de 5 objetos de estudiante y guardados en students.db ')
    print(f'Archivo cerrado: {file.closed} ')
    print('El numero de estudiantes en la clase es: ' + str(estudiante.number_of_students))
    print('Alumnos guardados')


def switch():
    while True:
        print('-----Menu-----')
        print('1- Guardar estudiante\n2- Leer estudiantes \n3- Actualizar estudiante\n4- Salir')
        sel= int(input('Escoja una opcion escribiendo su numero aqui: '))
        if sel== 1:
            guardar()
        elif sel== 2:
            leer()
        elif sel == 3:
            actualizar()
        elif sel == 4:
            print('La salida sera inminente...')
            break
        else:
            print("Error")



if __name__ == '__main__':
    crearguardar5objest()
    switch()




