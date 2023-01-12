class Fecha:
    def __init__(self, fecha):
        self.__fecha = fecha
        self.dia = fecha.split("/")[0]
        self.mes = fecha.split("/")[1]
        self.anio = fecha.split("/")[2]
    def dia(self):
        return self.__fecha.split("/")[0]
    def mes(self):
        return self.__fecha.split("/")[1]
    def anio(self):
        return self.__fecha.split("/")[2]
    def __str__(self) -> str:
        return self.__fecha