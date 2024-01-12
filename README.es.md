# **Proyecto Indice de Calidad del Aire 🌍🔍**
---
## *Descripción del Proyecto*

Este proyecto tiene como objetivo analizar y visualizar datos relacionados con la calidad del aire, centrándose en el Índice de Calidad del Aire (AQI, por sus siglas en inglés) y evaluando el nivel de riesgo asociado con los valores contaminantes. Además, se integran datos meteorológicos para una comprensión más completa del entorno.
Los datos utilizados en este proyecto han sido obtenidos de la Comunidad de Madrid. Estos datos proporcionan información detallada sobre la calidad del aire en diferentes municipios de la región.


## Descripción de los Datos

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

| CÓDIGO | MAGNITUD                         | DESCRIPCIÓN MAGNITUD | CÓDIGO TÉCNICA DE MEDIDA | DESCRIPCIÓN TÉCNICA DE MEDIDA | UNIDAD | DESCRIPCIÓN UNIDAD                |
|--------|---------------------------------|----------------------|---------------------------|-----------------------------|--------|----------------------------------|
| 1      | Dióxido de azufre               | Fluorescencia ultravioleta | 38                        | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 6      | Monóxido de carbono             | Espectrometría infrarroja no dispersiva | 48            | miligramos por metro cúbico | mg/m³  | miligramos por metro cúbico       |
| 7      | Monóxido de nitrógeno           | Quimioluminiscencia    | 8                         | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 8      | Dióxido de nitrógeno            | Quimioluminiscencia    | 8                         | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 9      | Partículas en suspensión < PM2,5| Absorción beta        | 49                        | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 10     | Partículas en suspensión < PM10 | Absorción beta        | 49                        | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 12     | Óxidos de nitrógeno             | Quimioluminiscencia    | 8                         | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 14     | Ozono                           | Absorción ultravioleta | 6                        | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 20     | Tolueno                         | Cromatografía de gases | 59                       | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 22     | Black Carbon                    | Absorción de luz        | 7                        | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 30     | Benceno                         | Cromatografía de gases | 59                       | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |
| 42     | Hidrocarburos totales           | Ionización llama        | 2                        | miligramos por metro cúbico | mg/m³  | miligramos por metro cúbico       |
| 44     | Hidrocarburos no metánicos      | Ionización llama        | 2                        | miligramos por metro cúbico | mg/m³  | miligramos por metro cúbico       |
| 431    | MetaParaXileno                  | Cromatografía de gases | 59                       | microgramos por metro cúbico | μg/m³  | microgramos por metro cúbico     |

#### **CLIMATOLÓGICOS** 

| CÓDIGO | MAGNITUD | DESCRIPCIÓN MAGNITUD | CÓDIGO DE TÉCNICA DE MEDIDA | UNIDAD | DESCRIPCIÓN UNIDAD |
|--------|----------|----------------------|-----------------------------|--------|---------------------|
| 81     | Velocidad del viento | m/s | 89 | metros por segundo |
| 82     | Dirección del viento | Grd | 89 | grados |
| 83     | Temperatura | ºC | 89 | grados centígrados |
| 86     | Humedad relativa | % | 89 | porcentaje |
| 87     | Presión atmosférica | mbar | 89 | milibar |
| 88     | Radiación solar | W/m² | 89 | vatios por metro cuadrado |
| 89     | Precipitación | l/m² | 89 | litros por metro cuadrado |

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
   git clone [https://github.com/Yakondra/Final-project-air-quality.git]
   o
   git clone [https://github.com/Pilizmt/Final-project-air-quality.git]

2. Instala las dependencias:

    ```bash
    pip install -r requirements.txt

## *Cómo Contribuir*

¡Las contribuciones son bienvenidas! Si encuentras problemas, tienes ideas para mejoras o deseas agregar nuevas características, siéntete libre de enviar un pull request. 🤝🚀
