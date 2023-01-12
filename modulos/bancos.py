import pandas as pd
from modulos.fecha import Fecha
from modulos.funciones import obtener_datos
class Bancos():
    def __init__(self, archivo: str, fecha: Fecha):
        try:
            self.fecha = fecha
            self.data = obtener_datos(archivo, fecha)

        except:
            raise "No se pudo leer el archivo"
    def filtro_fecha(self, fecha: Fecha) -> pd.DataFrame:
        data = self.data
        return data[(data['mes']== int(fecha.mes)) & (data['anho'] == int(fecha.anio))]
    
    def filtro_fecha_cuenta( self, fecha: Fecha, cuenta: str) -> float:
        data = self.data
        data=  data[(data['mes']== int(fecha.mes)) & (data['anho'] == int(fecha.anio))  & (data['cuenta'].str.contains(cuenta)) & (data['banco']=="SISTEMA")]
        return data['total'].values[0]
    def bank_count(self):
        data = self.data['balances']
        return data['banco'].nunique() - 1

