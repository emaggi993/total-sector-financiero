from modulos.funciones import obtener_datos
from modulos.fecha import Fecha
from modulos.bancos import Bancos
from modulos.informe import datos_informe
import os
import pandas as pd
import numpy as np

fecha = Fecha("01/01/2022")
archivo= "./datos/BOLB_BANCOS.xlsx"
archivo_total = "./datos/Total Sistema Financiero Base.xlsx"
path = os.path.realpath(archivo_total)
# master = tabla_master("Lista de cuentas.xlsx")
url_master= "Lista de cuentas.xlsx"
url_datos= "./datos/BOLB_BANCOS.xlsx"
result = datos_informe(url_master, url_datos)
f,c = result.head(40).shape
for fila in range(f):
    try:
        d = result.iloc[fila].dropna()
        # f = d[0]
        print("--"*30)
        print(d['fila'], d[d['hoja']])
    except KeyError:
        pass
    # for item in d[1:]:
    #     if item != np.nan:
    #         print(item)

    # print(f, 
    # d[-1] )
