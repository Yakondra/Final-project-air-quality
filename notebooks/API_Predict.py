import streamlit as st 
from pickle import load
import pickle

dicc_area = load(open('../data/interim/diccionarios/dicc_area.pk', 'rb'))

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