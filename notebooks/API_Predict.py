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

#Users data

media_val = st.slider('Introduzca el valor recogido:',
                    min_value = 0.04,
                    max_value = 800.00,
                    step = 0.01
                    )

municipio_val = st.selectbox('Seleccione el municipio:',
                       ('MADRID', 'ATAZAR (EL)')
                       )

bmi_val = st.slider('Enter your BMI:',
                    min_value = 15.80,
                    max_value = 51.20,
                    step = 0.01
                    )

children_val = st.number_input('Enter the number of children (if you have them):',
                               min_value = 0,
                               max_value = 5,
                               step = 1
                               )



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