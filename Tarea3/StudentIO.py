import os


try:
    import cPickle as pickle
except ImportError:
    import pickle

class estudiante:
    numero_de_estudiantes = 0
    nua = ''
    nombre = ''
    correo = ''
    contrasena = ''

    def __init__(self, nua='', nombre='', correo='', contrasena=''):
        self.nua = nua
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        estudiante.numero_de_estudiantes += 1


class estudiante_actualizacion:  # Se crea esta otra clase para que no afecte el contador de objetos de clase (numero_de_estudiantes)
    nua = ''
    nombre = ''
    correo = ''
    contrasena = ''

    def __init__(self, nua='', nombre='', correo='', contrasena=''):
        self.nua = nua
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena


def guardar():
    nua_inicial = input('Ingrese el numero unico de alumno (NUA): ')
    file1 = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file1)
    v = estudiante.numero_de_estudiantes
    for i in range(v):
        read_alumno = unpickler.load()
        if nua_inicial == read_alumno.nua:
            file1.close()
            print('NUA ya registrado, por favor vuelva a escoger la opcion 1-Guardar estudiante  del Menu e ingrese otro NUA diferente')
            switch()
        else:
            continue
    file1.close()
    nua = nua_inicial
    nombre = input('Ingrese el nombre: ')
    correo = input('Ingrese el correo: ')
    contrasena = input('Ingrese la contrasena: ')
    ObjetoE = estudiante(nua, nombre, correo, contrasena)
    file2 = open('students.db', 'ab+')
    pickle.dump(ObjetoE, file2)
    file2.close()
    print(f'Archivo cerrado: {file2.closed} ')
    print('El numero de estudiantes en la clase es: ' + str(estudiante.numero_de_estudiantes))
    print('Alumno guardado')


def leer():
    file3 = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file3)
    v = estudiante.numero_de_estudiantes
    for i in range(v):
        read_alumno = unpickler.load()
        print(f' NUA: {read_alumno.nua}')
        print(f' Nombre: {read_alumno.nombre}')
        print(f' Correo: {read_alumno.correo}')
        print(f' Contrasena: {read_alumno.contrasena}')
    file3.close()
    print('El numero de estudiantes en la clase es: ' + str(estudiante.numero_de_estudiantes))
    print('Alumnos mostrados')


def actualizar():
    nua_inicial = input('Ingrese el numero unico de alumno (NUA): ')
    file4 = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file4)
    v = estudiante.numero_de_estudiantes
    j = 0
    for i in range(v):
        read_alumno = unpickler.load()
        j += 1
        if nua_inicial == read_alumno.nua:
            break
        elif (j == v) and (nua_inicial != read_alumno.nua):
            file4.close()
            print('NUA no encontrado, por favor vuelva a escoger la opcion 3-Actualizar estudiante  del Menu e ingrese un NUA registrado')
            switch()
        else:
            continue
    file4.close()
    file5 = open('students.db', 'rb')
    unpickler = pickle.Unpickler(file5)
    v = estudiante.numero_de_estudiantes
    for i in range(v):
        read_alumno = unpickler.load()
        if nua_inicial == read_alumno.nua:
            nua = nua_inicial
            nombre = input('Ingrese el nombre: ')
            correo = input('Ingresa el correo: ')
            contrasena = input('Ingrese la contrasena: ')
            file6 = open('students.tmp', 'ab+')
            ObjetoE = estudiante_actualizacion(nua, nombre, correo, contrasena)
            pickle.dump(ObjetoE, file6)
            file6.close()
        else:
            nua = read_alumno.nua
            nombre = read_alumno.nombre
            correo = read_alumno.correo
            contrasena = read_alumno.contrasena
            file7 = open('students.tmp', 'ab+')
            ObjetoE = estudiante_actualizacion(nua, nombre, correo, contrasena)
            pickle.dump(ObjetoE, file7)
            file7.close()
    file5.close()
    os.unlink("students.db")
    my_file = 'students.tmp'
    base = os.path.splitext(my_file)[0]
    os.rename(my_file, base + '.db')
    print('Alumno guardado')


def crearguardar5objest():  # crear 5 objetos de estudiante y guardarlos en students.db
    ObjetoE1 = estudiante('703270', 'David Fernando Ortega Tamayo', 'df.ortegatamayo@ugto.mx', '123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE1, file)
    file.close()
    ObjetoE2 = estudiante('703271', 'Jose Amparo Andrade Lucio', 'andrade@ugto.mx', 'wadaw22')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE2, file)
    file.close()
    ObjetoE3 = estudiante('703272', 'Roberto Rojas Laguna', 'rr.rojaslaguna@ugto.mx', '1d2d23456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE3, file)
    file.close()
    ObjetoE4 = estudiante('703273', 'Oscar Ibarra Almanza', 'oscar@ugto.mx', '33d123456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE4, file)
    file.close()
    ObjetoE5 = estudiante('703274', 'Estudillo Ayala Ramirez', 'estudillo@ugto.mx', '1dd223456')
    file = open('students.db', 'ab+')
    pickle.dump(ObjetoE5, file)
    file.close()
    print('Creacion de 5 objetos de estudiante y guardados en students.db ')
    print(f'Archivo cerrado: {file.closed} ')
    print('El numero de estudiantes en la clase es: ' + str(estudiante.numero_de_estudiantes))
    print('Alumnos guardados')


def switch():
    while True:
        print('-----Menu-----')
        print('1- Guardar estudiante\n2- Leer estudiantes \n3- Actualizar estudiante\n4- Salir')
        sel = int(input('Escoja una opcion escribiendo su numero aqui: '))
        if sel == 1:
            guardar()
        elif sel == 2:
            leer()
        elif sel == 3:
            actualizar()
        elif sel == 4:
            print('La salida sera inminente...')
            exit()
        else:
            print("Error")
