import pandas as pd
from modulos.fecha import Fecha

def leer_informe_bancos(url: str) :
    datos = pd.read_excel(url, sheet_name="BANCOS", header= None)
    datos= datos.iloc[5:]
    cuentas = datos[0]
    cuentas.dropna(how="all", inplace= True)
    cuentas.to_excel("Lista de cuentas.xlsx")
    print(cuentas)
def tabla_master(url) -> pd.DataFrame:
    datos = pd.read_excel(url, sheet_name='master')
    print( datos.head())
    return datos
def bank_count(archivo, hojas, fecha) -> int:
    datos = pd.read_excel(archivo, sheet_name= hojas)
    datos = datos[(datos['mes']== int(fecha.mes))&(datos['anho']==int(fecha.anio)) ]
    return datos['banco'].nunique() - 1
def datos_balances_exc_bnf(url_master, url_datos, fecha: Fecha):
    balances = pd.read_excel(url_datos, sheet_name="balances")
    sistema = balances[(balances['mes']== int(fecha.mes))&(balances['anho']==int(fecha.anio)) & (balances['banco']=='SISTEMA')]
    bnf = balances[(balances['mes']== int(fecha.mes))&(balances['anho']==int(fecha.anio)) & (balances['banco']=='Banco Nacional de Fomento')]
    sistema = sistema[['cuenta', 'MN', 'ME', 'total']]
    sistema = sistema.rename(columns={'MN':'sistema-mn', 'ME': 'sistema-me', 'total':'sistema-total'})
    bnf = bnf[['cuenta', 'MN', 'ME', 'total']]
    bnf = bnf.rename(columns={'MN':'bnf-mn', 'ME': 'bnf-me', 'total':'bnf-total'})
    balance_exc_bnf= pd.merge(sistema, bnf, how='inner', on='cuenta')

    balance_exc_bnf['balances-exc-bnf-me']= balance_exc_bnf['sistema-me'] - balance_exc_bnf['bnf-me']
    balance_exc_bnf['balances-exc-bnf-mn']= balance_exc_bnf['sistema-mn'] - balance_exc_bnf['bnf-mn']
    balance_exc_bnf['balances-exc-bnf']= balance_exc_bnf['sistema-total'] - balance_exc_bnf['bnf-total']
    balance_exc_bnf= balance_exc_bnf[['cuenta','balances-exc-bnf-me', 'balances-exc-bnf-mn', 'balances-exc-bnf']]
def datos_informe(url_master, url_datos, fecha: Fecha):
    master = pd.read_excel(url_master, sheet_name="master")

    adicional = pd.read_excel(url_datos, sheet_name="adicional")
    adicional = adicional[(adicional['mes']== int(fecha.mes))&(adicional['anio']== int(fecha.anio)) & (adicional['banco']=='Sistema')]
    adicional = adicional[['cuenta', 'val_num']]
    adicional = adicional.rename(columns={'val_num':'adicional'})

    balances = pd.read_excel(url_datos, sheet_name="balances")
    sistema = balances[(balances['mes']== int(fecha.mes))&(balances['anho']==int(fecha.anio)) & (balances['banco']=='SISTEMA')]
    bnf = balances[(balances['mes']== int(fecha.mes))&(balances['anho']==int(fecha.anio)) & (balances['banco']=='Banco Nacional de Fomento')]
    balances = balances[(balances['mes']== int(fecha.mes))&(balances['anho']==int(fecha.anio)) & (balances['banco']=='SISTEMA')]
    balances = balances [['cuenta', 'total', 'MN', 'ME']]
    balances = balances.rename(columns={'total': 'balances', 'MN':'balances-MN', 'ME':'balances-ME'})

    sistema = sistema[['cuenta', 'MN', 'ME', 'total']]
    sistema = sistema.rename(columns={'MN':'sistema-mn', 'ME': 'sistema-me', 'total':'sistema-total'})
    bnf = bnf[['cuenta', 'MN', 'ME', 'total']]
    bnf = bnf.rename(columns={'MN':'bnf-mn', 'ME': 'bnf-me', 'total':'bnf-total'})
    balance_exc_bnf= pd.merge(sistema, bnf, how='inner', on='cuenta')

    balance_exc_bnf['balances-exc-bnf-me']= balance_exc_bnf['sistema-me'] - balance_exc_bnf['bnf-me']
    balance_exc_bnf['balances-exc-bnf-mn']= balance_exc_bnf['sistema-mn'] - balance_exc_bnf['bnf-mn']
    balance_exc_bnf['balances-exc-bnf']= balance_exc_bnf['sistema-total'] - balance_exc_bnf['bnf-total']
    balance_exc_bnf= balance_exc_bnf[['cuenta','balances-exc-bnf-me', 'balances-exc-bnf-mn', 'balances-exc-bnf']]

    # print("****"*10, balance_exc_bnf.shape)

    estados = pd.read_excel(url_datos, sheet_name="estados")
    estados = estados[(estados['mes']== int(fecha.mes))&(estados['anho']==int(fecha.anio)) & (estados['banco']=='Sistema')]
    estados = estados [['cuenta', 'total', 'MN', 'ME']]
    estados = estados.rename(columns={'total': 'estados', 'MN':'estados-MN', 'ME':'estados-ME'})

    ratios = pd.read_excel(url_datos, sheet_name="ratios")
    ratios = ratios[(ratios['mes']== int(fecha.mes))&(ratios['anio']== int(fecha.anio)) & (ratios['banco']=='Sistema')]
    ratios = ratios[['cuentas', 'valor']]
    ratios = ratios.rename(columns={'valor':'ratios', 'cuentas': 'cuenta'})

    tarjeta = pd.read_excel(url_datos, sheet_name="tarjeta")
    tarjeta = tarjeta[(tarjeta['mes_num']== int(fecha.mes))&(tarjeta['anio']== int(fecha.anio)) ]
    tarjeta = tarjeta[['Bancos', 'valor']]
    tarjeta = tarjeta.rename(columns={'valor':'tarjeta', 'Bancos': 'cuenta'})

    tarjeta_cantidad = pd.read_excel(url_datos, sheet_name="tarjeta_cantidad")
    tarjeta_cantidad = tarjeta_cantidad[(tarjeta_cantidad['mes_num']== int(fecha.mes))&(tarjeta_cantidad['anio']== int(fecha.anio)) ]
    tarjeta_cantidad = tarjeta_cantidad[['Bancos', 'valor']]
    tarjeta_cantidad = tarjeta_cantidad.rename(columns={'valor':'tarjeta_cantidad', 'Bancos': 'cuenta'})

    result = pd.merge(master, adicional, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, balances, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, estados, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, ratios, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, tarjeta, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, tarjeta_cantidad, how='left' , left_on='cuenta', right_on='cuenta')

    result = pd.merge(result, balance_exc_bnf, how='left' , left_on='cuenta', right_on='cuenta')

    # print("*--**--*"*10, result.shape)

    return result