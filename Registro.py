class Registro:
    __temperatura = ""
    __humedad = ""
    __presion_atmosferica = ""

    def __init__(self, temperatura, humedad, presion_atmosferica):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion_atmosferica = presion_atmosferica

    def getTemperatura(self):
        return int(self.__temperatura)

    def getHumedad(self):
        return int(self.__humedad)

    def getPresion(self):
        return int(self.__presion_atmosferica)

    def __str__(self):
        return str(self.__temperatura+" "+self.__humedad+" "+self.__presion_atmosferica+" ")
