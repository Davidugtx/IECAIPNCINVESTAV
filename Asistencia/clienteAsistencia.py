
import socket
import pickle
from estudiante import Estudiante


def main():
    s=socket.socket()
    host = '3.16.226.150'
    port = 9999

    s.connect((host, port))
    estudiante = Estudiante('David Fernando Ortega Tamayo', 'df.ortegatamayo@ugto.mx', 'Pycharm')

    estudiante_seriado = pickle.dumps(estudiante)
    s.send(estudiante_seriado)
    res = s.recv(1024)

    print(f' respuesta: \n\t{res.decode()}')
    s.close()

if __name__ == '__main__':
    main()