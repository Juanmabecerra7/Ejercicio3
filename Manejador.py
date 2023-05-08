from Registro import Registro
import csv


class Manejador:
    def __init__(self, D, T):
        self.__lista = [[Registro for _ in range(T)] for _ in range(D)]

    def agregarregistro(self, dia, hora, unregistro):
        self.__lista[dia - 1][hora - 1] = unregistro

    def minTemperatura(self, D, T):
        min = 100
        i = 0
        while i < D:
            j = 0
            while j < T:
                if int(Registro.getTemperatura(self.__lista[i][j])) < min:
                    min = int(Registro.getTemperatura(self.__lista[i][j]))
                    Dia = i+1
                    Hora = j+1
                j = j + 1
            i = i + 1
        print(f"Los Datos con mas baja temperatura es el DIA: {Dia}, a la HORA: {Hora}")

    def minHumedad(self, D, T):
        min = 100
        i = 0
        while i < D:
            j = 0
            while j < T:
                if int(Registro.getHumedad(self.__lista[i][j])) < min:
                    min = int(Registro.getHumedad(self.__lista[i][j]))
                    Dia = i+1
                    Hora = j+1
                j = j + 1
            i = i + 1
        print(f"Los Datos con mas baja Humedad es el DIA: {Dia}, a la HORA: {Hora}")

    def minPresion(self, D, T):
        min = 100
        i = 0
        while i < D:
            j = 0
            while j < T:
                if int(Registro.getPresion(self.__lista[i][j])) < min:
                    min = int(Registro.getPresion(self.__lista[i][j]))
                    Dia = i + 1
                    Hora = j + 1
                j = j + 1
            i = i + 1
        print(f"El Datos con mas baja Presion Atmosferica es el DIA: {Dia}, a la HORA: {Hora}")
        
    def temperaturaPromedio(self, D, T):
        i = 0
        while i < T:
            j = 0
            promedio = 0
            total = 0
            while j < D:
                total = Registro.getTemperatura(self.__lista[j][i]) + total
                j = j + 1
            promedio = total / T
            print("La temperatura promedio en la Hora {} es de {}".format(i+1, promedio))
            i = i + 1


    def mostarDia(self, dia, D, T):
        i = 0
        while i < D:
            if i == dia:
                j = 0
                while j < T:
                    print("HORA TEMPERATURA HUMEDAD PRESION")
                    print (str(j+1)+" "+str(Registro.getTemperatura(self.__lista[dia][j]))+" "+str(Registro.getHumedad(self.__lista[dia][j]))+" "+str(Registro.getPresion(self.__lista[dia][j])))
                    j = j + 1
            i = i + 1


    def test(self):
        archivo = open("registros.csv")
        reader = csv.reader(archivo, delimiter=",")
        for fila in reader:
            dia = int(fila[0])
            hora = int(fila[1])
            temperatura = fila[2]
            humedad = fila[3]
            presion_atmosferica = fila[4]
            unregistro = Registro(temperatura, humedad, presion_atmosferica)
            self.agregarregistro(dia, hora, unregistro)
        archivo.close()

    def mostrar(self, D, T):
        s = ""
        i = 0
        while i < D:
            print(f"DIA: {i+1}")
            j = 0
            while j < T:
                print(f"HORA: {j+1}")
                print(str(self.__lista[i][j]))
                j = j + 1
            i = i + 1
