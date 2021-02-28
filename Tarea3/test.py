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


ObjetoE1=estudiante('703270', 'David Fernando Ortega Tamayo', 'df.ortegatamayo@ugto.mx', '123456')
print(ObjetoE1.nombre)

ObjetoE1.nombre='Raul'
print(ObjetoE1.nombre)
