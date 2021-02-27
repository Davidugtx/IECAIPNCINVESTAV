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
    nua = input('Ingrese el numero unico de alumno (nua): ')
    nombre = input('Ingrese el nombre: ')
    correo = input('Ingrese el correo: ')
    contrasena = input('Ingrese la contrasena: ')
    ObjetoE = estudiante(nua, nombre, correo, contrasena)
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
    NUA=input('Ingrese el numero unico de alumno (nua): ')
    file = open('students.db', 'rb+')

    unpickler = pickle.Unpickler(file)
    v = estudiante.number_of_students


    read_alumno = unpickler.load()
    if NUA == read_alumno.nua:
        nombre = input('Ingrese el nombre: ')
        correo = input('Ingrese el correo: ')
        contrasena = input('Ingrese la contrasena: ')
        ObjetoE = estudiante(NUA, nombre, correo, contrasena)
        file = open('students.temp', 'ab+')
        pickle.dump(ObjetoE, file)
        file.close()
        print(f'Archivo cerrado: {file.closed} ')
    else:
        print('NUA no encontrado')

    print('Datos del estudiante actualizado')

def crearguardar5objest():  #crear 5 objetos de estudiante y guardarlos en students.db
    ObjetoE = estudiante('703270', 'David Fernando Ortega Tamayo', 'df.ortegatamayo@ugto.mx', '123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    ObjetoE = estudiante('703271', 'Jose Amparo Andrade Lucio', 'andrade@ugto.mx', 'wadaw22')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    ObjetoE = estudiante('703272', 'Roberto Rojas Laguna', 'rr.rojaslaguna@ugto.mx', '1d2d23456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    ObjetoE = estudiante('703273', 'Oscar Ibarra Almanza', 'oscar@ugto.mx', '33d123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    ObjetoE = estudiante('703274', 'Estudillo Ayala Ramirez', 'estudillo@ugto.mx', '1dd223456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file)
    file.close()
    print('Creacion de 5 objetos de estudiante y guardados en students.db ')
    print(f'Archivo cerrado: {file.closed} ')
    print('El numero de estudiantes en la clase es: ' + str(estudiante.number_of_students))
    print('Alumnos guardados')


def switch():
    while True:
        print('-----Menu-----')
        print('1- Guardar estudiante\n2- Leer estudiante \n3- Actualizar estudiante\n4- Salir')
        sel= int(input('Escoja una opcion escribiendo su numero aqui: '))
        if sel== 1:
            guardar()
            continue
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



