import streamlit as st 
from pickle import load
import pickle

dicc_area = load(open('../data/interim/diccionarios/dicc_area.pk', 'rb'))
dicc_ccaa = load(open('../data/interim/diccionarios/dicc_ccaa.pk', 'rb'))
dicc_estacion = load(open('../data/interim/diccionarios/dicc_estacion.pk', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/dicc_magnitudes.pk', 'rb'))
dicc_municipios = load(open('../data/interim/diccionarios/dicc_municipios.pk', 'rb'))
dicc_provincias = load(open('../data/interim/diccionarios/dicc_provincias.pk', 'rb'))


st.title('Nivel de peligrosidad de contaminantes atmosféricos')
# Introductory message
st.write('Introduzca los siguientes valores para iniciar.')



# input_data = {
#     'LATITUD': valor_latitud,
#     'LONGITUD': valor_longitud,
#     'MEDIA_DIARIA': valor_media_diaria,
#     'N_MUNICIPIO_N': valor_municipio,
#     'MAGNITUD_N': valor_magnitud,
#     'TIPO_AREA_N': valor_tipo_area,
#     'TIPO_ESTACION_N': valor_tipo_estacion,
#     'PELIGROSIDAD_N': valor_peligrosidad
# }