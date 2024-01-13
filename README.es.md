# **Proyecto Indice de Calidad del Aire 🌍🔍**
---
## *Descripción del Proyecto*

Este proyecto tiene como objetivo analizar y visualizar datos relacionados con la calidad del aire, centrándose en el Índice de Calidad del Aire (AQI, por sus siglas en inglés) y evaluando el nivel de riesgo asociado con los valores contaminantes. Además, se integran datos meteorológicos para una comprensión más completa del entorno.
Los datos utilizados en este proyecto han sido obtenidos de la Comunidad de Madrid. Estos datos proporcionan información detallada sobre la calidad del aire en diferentes municipios de la región.

Los datos han sido recopilados y compartidos por la Comunidad de Madrid como parte de su iniciativa de monitoreo de la calidad del aire. Puedes encontrar más información y acceder a los conjuntos de datos originales en el sitio web oficial de la Comunidad de Madrid (https://datos.comunidad.madrid/catalogo/organization/comunidad-de-madrid).

Agradecemos a la Comunidad de Madrid por proporcionar estos datos valiosos que han permitido llevar a cabo este análisis sobre la calidad del aire.

## *Descripción de los Datos*

#### **ESTRUCTURA DE LOS ARCHIVOS**

- provincia: Número que representa la provincia.
- municipio: Número que identifica el municipio.
- estacion: Número de la estación de monitoreo.
- magnitud: Código que indica la magnitud medida.
- punto_muestreo: Identificación específica del punto de muestreo.
- ano, mes, dia: Año, mes y día de la medición.
- h01 a h24: Concentraciones horarias respectivas para cada hora del día.
- v01 a v24: Valores asociados a las concentraciones, representados como 'V'.

#### **CONTAMINANTES**

| CÓDIGO | MAGNITUD                         | DESCRIPCIÓN MAGNITUD | 
|--------|---------------------------------|----------------------| 
| 1      | Dióxido de azufre               | Fluorescencia ultravioleta | 
| 6      | Monóxido de carbono             | Espectrometría infrarroja no dispersiva | 
| 7      | Monóxido de nitrógeno           | Quimioluminiscencia    | 
| 8      | Dióxido de nitrógeno            | Quimioluminiscencia    | 
| 9      | Partículas en suspensión < PM2,5| Absorción beta        | 
| 10     | Partículas en suspensión < PM10 | Absorción beta        | 
| 12     | Óxidos de nitrógeno             | Quimioluminiscencia    | 
| 14     | Ozono                           | Absorción ultravioleta | 
| 20     | Tolueno                         | Cromatografía de gases | 
| 22     | Black Carbon                    | Absorción de luz        | 
| 30     | Benceno                         | Cromatografía de gases | 
| 42     | Hidrocarburos totales           | Ionización llama        | 
| 44     | Hidrocarburos no metánicos      | Ionización llama        | 
| 431    | MetaParaXileno                  | Cromatografía de gases | 

> Todos los datos de concentración están expresados en microgramos por metro cúbico (μg/m³).


#### **CLIMATOLÓGICOS** 

| CÓDIGO | MAGNITUD               | DESCRIPCIÓN MAGNITUD | 
|--------|------------------------|----------------------| 
| 81     | Velocidad del viento   | m/s                  | 
| 82     | Dirección del viento   | Grd                  | 
| 83     | Temperatura            | ºC                   | 
| 86     | Humedad relativa       | %                    | 
| 87     | Presión atmosférica    | mbar                 | 
| 88     | Radiación solar        | W/m²                 | 
| 89     | Precipitación          | l/m²                 | 


#### **MUNICIPIOS**

| ID    | Municipio            | ID    | Municipio                | ID    | Municipio                | ID    | Municipio                |
|-------|----------------------|-------|--------------------------|-------|--------------------------|-------|--------------------------|
| 5     | ALCALÁ DE HENARES    | 49    | COSLADA                  | 74    | LEGANÉS                  | 102   | ORUSCO DE TAJUÑA         |
| 6     | ALCOBENDAS           | 58    | FUENLABRADA              | 80    | MAJADAHONDA              | 120   | PUERTO DE COTOS          |
| 7     | ALCORCÓN             | 65    | GETAFE                   | 92    | MÓSTOLES                 | 123   | RIVAS-VACIAMADRID        |
| 9     | ALGETE               | 67    | GUADALIX DE LA SIERRA    | 74    | LEGANÉS                  | 133   | SAN MARTÍN DE VALDEIGLESIAS |
| 13    | ARANJUEZ             |-------|--------------------------| 80    | MAJADAHONDA              | 148   | TORREJÓN DE ARDOZ        |
| 14    | ARGANDA DEL REY      |       |                          | 92    | MÓSTOLES                 | 161   | VALDEMORO                |
| 16    | EL ATAZAR            |       |                          | 102   | ORUSCO DE TAJUÑA         | 171   | VILLA DEL PRADO          |
| 45    | COLMENAR VIEJO       |       |                          | 120   | PUERTO DE COTOS          | 180   | VILLAREJO DE SALVANÉS    |
| 47    | COLLADO VILLALBA     |       |                          | 123   | RIVAS-VACIAMADRID        |       |                          |



## *Características Principales*

- Análisis de datos de calidad del aire.
- Cálculo y representación del AQI.
- Evaluación del nivel de riesgo asociado con los valores contaminantes.
- Integración de datos meteorológicos.
- Visualización de datos a través de gráficos y tablas.
- Creación y entrenamiento de un modelo de machine learning para predecir el AQI.

## *Tecnologías Utilizadas*

- Python 🐍
- Pandas 🐼
- Matplotlib/Seaborn 📊
- Scikit-learn (para el modelo de machine learning).
- Otros módulos relevantes para análisis de datos y visualización.
- API de datos meteorológicos (por ejemplo, OpenWeatherMap). 🌦️

## *Estructura del Proyecto*

- `data/`: Carpeta que contiene los conjuntos de datos utilizados, procesados y temporales.
- `models/`: Carpeta que contiene los modelos de machine learning.
- `src/`: Carpeta que contiene el código fuente del proyecto.
- `README.md`: Documentación del proyecto (este archivo). 📚

## *Instrucciones de Ejecución*

1. Clona este repositorio:

   ```bash
   git clone (https://github.com/Yakondra/Final-project-air-quality.git)
   o
   git clone (https://github.com/Pilizmt/Final-project-air-quality.git)

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

## *Cómo Contribuir*

¡Las contribuciones son bienvenidas! Si encuentras problemas, tienes ideas para mejoras o deseas agregar nuevas características, siéntete libre de enviar un pull request. 🤝🚀
