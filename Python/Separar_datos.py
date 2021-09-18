''' import os
import pandas as pd

def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    sum_edades_est = 0
    c_edades_est = 0
    cant_tipo = data['Tipo'].value_counts(dropna = False)
    tipo = data['Tipo']
    edad = data['Edad']
    for tipo, edad in zip(tipo, edad):
        if tipo == 'En estudio':
            sum_edades_est += edad
            c_edades_est += 1
    dic = {
        'casos_en_estudio': cant_tipo[1],
        'prom_edades_casos_en_estudio': int(sum_edades_est / c_edades_est),
    }
    return dic

print(analisis_datos(
    (pd.read_csv('https://bitbucket.org/ingluise2019/misiontic/downloads/Casos_positivos_de_COVID-19_en_Colombia.csv').sample(frac=1.0, random_state=123)))) '''

# print(analisis_datos(
#     (pd.read_csv(os.path.dirname(__file__) + '/Casos_positivos_de_COVID-19_en_Colombia.csv').sample(frac=1.0, random_state=123))))
"""
{'casos_en_estudio': 4558, 
'prom_edades_casos_en_estudio'
: 42, 'casos_importados': 813, 
'prom_edades_casos_importados'
: 42, 'casos_relacionados': 4589, 
'prom_edades_casos_relacionado
s': 37, 'total_casos': 9960}"""


'''{'casos_en_estudio': 4558, 'prom_edades_casos_en_estudio': 42}, {'casos_en_importado': 813, 'prom_edades_casos_importado': 42}, {'casos_relacionados': 4589, 'prom_edades_casos_relacionados': 37}'''

import os
import pandas as pd
def analisis_datos(data: pd.core.frame.DataFrame)->dict:
    sum_edades_est = 0
    c_edades_est = 0
    sum_edades_imp = 0
    c_edades_imp = 0
    sum_edades_rel = 0
    c_edades_rel = 0
    cant_tipo = data['Tipo'].value_counts(dropna = False)
    tipo = data['Tipo']
    edad = data['Edad']
    for tipo, edad in zip(tipo, edad):
        if tipo == 'En estudio':
            sum_edades_est += edad
            c_edades_est += 1
        if tipo == 'Importado':
            sum_edades_imp += edad
            c_edades_imp += 1
        if tipo == 'Relacionado':
            sum_edades_rel += edad
            c_edades_rel += 1
    dic = {
    'casos_en_estudio': cant_tipo[1],
    'prom_edades_casos_en_estudio': int(sum_edades_est / c_edades_est),
    'casos_importados': cant_tipo[2],
    'prom_edades_casos_importados': int(sum_edades_imp / c_edades_imp),
    'casos_relacionados': cant_tipo[0],
    'prom_edades_casos_relacionados': int(sum_edades_rel / c_edades_rel),
    'total_casos': cant_tipo[1] + cant_tipo[2] + cant_tipo[0]
    }
    return dic

	
print(analisis_datos(
    (pd.read_csv('https://bitbucket.org/ingluise2019/misiontic/downloads/Casos_positivos_de_COVID-19_en_Colombia.csv').sample(frac=0.25, random_state=123))))
