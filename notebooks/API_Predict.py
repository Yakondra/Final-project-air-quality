import streamlit as st 
from pickle import load


dicc_municipality = load(open('../data/interim/diccionarios/N_MUNICIPIO_dicc.pk', 'rb'))
dicc_magnitudes = load(open('../data/interim/diccionarios/MAGNITUD_dicc.pk', 'rb'))
dicc_area = load(open('../data/interim/diccionarios/TIPO_AREA_dicc.pk', 'rb'))
dicc_station = load(open('../data/interim/diccionarios/TIPO_ESTACION_dicc.pk', 'rb'))
dicc_peligrosidad = load(open('../data/interim/diccionarios/PELIGROSIDAD_dicc.pk', 'rb'))


st.title('Nivel de peligrosidad de contaminantes atmosféricos')
# Introductory message
st.write('Introduzca los siguientes valores para iniciar.')

#Users data

mean_value = st.slider('Introduzca el valor recogido:',
                    min_value = 0.04,
                    max_value = 800.00,
                    step = 0.01
                    )

sel_municip = st.selectbox('Seleccione el municipio:', options= list(dicc_municipality.keys()))

sel_magnitud = st.selectbox('Seleccione el contaminante:', options= list(dicc_magnitudes.keys()))

sel_area = st.selectbox('Seleccione el tipo de área:', options= list(dicc_area.keys()))

sel_station = st.selectbox('Seleccione el tipo de estación:', options= list(dicc_station.keys()))


# Load factorized values

fact_values = load(open('../data/interim/factorize_values/sin_LL.pk', 'rb'))

# Button to predict

row = [mean_value,
    fact_values["N_MUNICIPIO_N"][sel_municip.lower()],
    fact_values["MAGNITUD_N"][sel_magnitud.lower()],
    fact_values["TIPO_AREA_N"][sel_area.lower()],
    fact_values["TIPO_ESTACION_N"][sel_station.lower()]
    ]

if st.button('Predict:'):

    model = load(open('../models/RandomForestMadrid_23.pk', 'rb'))
    y_pred = model.predict([row])

    st.text('Peligrosidad:' +str(round(y_pred[0, 0], 2)))




# # Opción seleccionada usando las claves del diccionario
# opcion_seleccionada = st.selectbox(
#     'Selecciona una opción:',
#     options=list(mi_diccionario.keys())
# )

# st.write(f'Has seleccionado: {opcion_seleccionada}')



# # Opción seleccionada usando los valores del diccionario
# opcion_seleccionada = st.selectbox(
#     'Selecciona una opción:',
#     options=list(mi_diccionario.values())
# )

# st.write(f'Has seleccionado: {opcion_seleccionada}')