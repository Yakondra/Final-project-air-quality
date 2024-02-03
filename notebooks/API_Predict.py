import streamlit as st 
from pickle import load

# Correspondence
dicc_municipality = {
        'ALCOBENDAS': 0,
        'ATAZAR (EL)': 1,
        'COLLADO VILLALBA': 2,
        'FUENLABRADA': 3,
        'MADRID': 4,
        'ALCALÁ DE HENARES': 5,
        'COLMENAR VIEJO': 6,
        'MÓSTOLES': 7,
        'ORUSCO DE TAJUÑA': 8,
        'VILLA DEL PRADO': 9,
        'VALDEMORO': 10,
        'RIVAS-VACIAMADRID': 11,
        'TORREJÓN DE ARDOZ': 12,
        'VILLAREJO DE SALVANÉS': 13,
        'ARGANDA DEL REY': 14,
        'COSLADA': 15,
        'GETAFE': 16,
        'LEGANÉS': 17,
        'MAJADAHONDA': 18,
        'ALCORCÓN': 19,
        'ALGETE': 20,
        'ARANJUEZ': 21,
        'RASCAFRÍA': 22,
        'SAN MARTÍN DE VALDEIGLESIAS': 23,
        'GUADALIX DE LA SIERRA': 24
}

dicc_magnitudes = {
        'C6H6': 0,
        'CO': 1,
        'NO2': 2,
        'NOX': 3,
        'O3': 4,
        'PM10': 5,
        'PM2.5': 6,
        'SO2': 7,
    }

dicc_area = {
        'URBANA': 0, 
        'RURAL': 1,
        'SUBURBANA': 2
}

dicc_station = {
        'TRAFICO': 0,
        'FONDO': 1,
        'INDUSTRIAL': 2
}

dicc_danger = {
        'Baja': 0,
        'Normal': 1,
        'Alta': 2
}


st.title('Nivel de peligrosidad de contaminantes atmosféricos')
# Introductory message
st.write('Introduzca los siguientes valores para iniciar.')

#Users data

mean_value = st.slider('Introduzca el valor recogido:',
                    min_value = 0.04,
                    max_value = 800.00,
                    step = 0.01
                    )

sel_municipality = st.selectbox('Seleccione el municipio:','Seleccione el municipio:', dicc_municipality)

sel_area = st.selectbox('Seleccione el tipo de área:', dicc_area)

sel_station = st.selectbox('Seleccione el tipo de estación:', dicc_station)

sel_magnitud = st.selectbox('Seleccione la magnitud:', dicc_magnitudes)

# Load factorized values

fact_values = load(open('../data/interim/factorize_values/facto_madrid.pk', 'rb'))

# Button to predict

row = [mean_value,
    fact_values["N_MUNICIPIO_N"][sel_municipality.lower()],
    fact_values["MAGNITUD_N"][sel_municipality.lower()],
    fact_values["TIPO_AREA_N"][sel_municipality.lower()],
    fact_values["TIPO_ESTACION_N"][sel_municipality.lower()]
    ]

if st.button('Predict:'):
    normal_scaler = load(open('../models/normal_scaler.pk', 'rb'))
    scaler_row = normal_scaler.transform([row])

    model = load(open('../models/linear_regression.pk', 'rb'))
    y_pred = model.predict([row])

    st.text('The price of the insurance would be:' +str(round(y_pred[0, 0], 2)))