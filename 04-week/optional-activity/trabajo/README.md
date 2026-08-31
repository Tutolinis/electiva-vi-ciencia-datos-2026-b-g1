# Actividad calificable · Corte 1 — Diagnóstico de datos de un proceso

## 1. Problema y pregunta de datos

### Proceso seleccionado
Gestión de reservas y ocupación de un hotel boutique.

### Problema
Un hotel boutique necesita gestionar adecuadamente sus reservas y conocer con anticipación la demanda de habitaciones. Cuando la información de reservas, cancelaciones, huéspedes y servicios se encuentra dispersa, puede ser difícil identificar patrones de ocupación y tomar decisiones oportunas sobre disponibilidad y recursos.

El objetivo del análisis es utilizar los datos históricos de las reservas para comprender el comportamiento de la demanda y anticipar la ocupación futura del hotel.

### Pregunta de datos
> **¿Cuál será la ocupación esperada del hotel durante las próximas semanas y qué patrones históricos de reservas pueden ayudar a anticipar la demanda de habitaciones?**

Esta pregunta permite utilizar información histórica para realizar una analítica predictiva, ya que busca estimar un comportamiento futuro a partir de datos anteriores. La analítica predictiva utiliza datos históricos y patrones anteriores para realizar pronósticos sobre resultados futuros.

---

## 2. Inventario de datos

Para responder la pregunta se necesitan diferentes fuentes de datos relacionadas con el proceso de reservas.

| # | Fuente / Campo | Descripción | Tipo de dato |
|---|---|---|---|
| 1 | **ID de reserva** | Identificador único de cada reserva | Estructurado |
| 2 | **Fecha de reserva** | Fecha en la que se realizó la reserva | Estructurado |
| 3 | **Fecha de entrada** | Día en que ingresa el huésped | Estructurado |
| 4 | **Fecha de salida** | Día en que finaliza la estadía | Estructurado |
| 5 | **Tipo de habitación** | Individual, doble, suite, etc. | Estructurado |
| 6 | **Tarifa por noche** | Precio de la habitación por noche | Estructurado |
| 7 | **Estado de reserva** | Confirmada, cancelada, completada, etc. | Estructurado |
| 8 | **Canal de reserva** | Página web, teléfono, agencia, plataforma externa, etc. | Semiestructurado |
| 9 | **Comentarios del huésped** | Opiniones y observaciones escritas por los clientes | No estructurado |
| 10 | **Registro de servicios** | Spa, restaurante, lavandería y otros servicios consumidos | Estructurado / Semiestructurado |

> Los datos estructurados se caracterizan por tener un modelo definido, mientras que los datos no estructurados no siguen necesariamente un esquema tabular; ejemplos de estos últimos incluyen textos, imágenes, audio y documentos. Los datos semiestructurados pueden contener metadatos o marcadores sin seguir completamente un modelo relacional.

### Clasificación resumida

* **Datos estructurados:**
  * ID de reserva
  * Fecha de reserva
  * Fecha de entrada
  * Fecha de salida
  * Tipo de habitación
  * Tarifa
  * Estado de reserva
  * Servicios consumidos

* **Datos semiestructurados:**
  * Canal de reserva
  * Registros provenientes de plataformas externas en formatos como JSON.

* **Datos no estructurados:**
  * Comentarios y opiniones de huéspedes.
  * Documentos o archivos adjuntos relacionados con las reservas.

---

## 3. Tipo de analítica

### Analítica predictiva
El tipo de analítica principal que se aplicará es **predictiva**.

La razón es que el objetivo no solamente es conocer qué ocurrió con las reservas anteriores, sino utilizar esos datos para estimar la ocupación futura del hotel.

Por ejemplo, a partir de variables como:
* Reservas históricas.
* Fechas de entrada y salida.
* Temporada.
* Día de la semana.
* Tipo de habitación.
* Cancelaciones.
* Canal de reserva.
* Número de huéspedes.

se podría construir un modelo que estime la cantidad de habitaciones que probablemente estarán ocupadas en un período futuro.

La analítica predictiva busca precisamente utilizar datos históricos y actuales para anticipar tendencias o resultados futuros.

### Analítica descriptiva como etapa previa
Antes de realizar la predicción también se utilizaría **analítica descriptiva** para responder preguntas como:
* ¿Cuántas habitaciones se ocuparon durante los últimos meses?
* ¿Cuál fue el porcentaje promedio de ocupación?
* ¿Qué días tuvieron mayor demanda?

Esto permite comprender el comportamiento histórico antes de construir una predicción.

La analítica descriptiva responde principalmente qué ocurrió, mientras que la predictiva busca estimar qué podría ocurrir posteriormente.

---

## 4. ¿Es un caso de Big Data?

No necesariamente en su alcance actual.

El proceso del hotel genera diferentes tipos de información y puede crecer con el tiempo, pero para un hotel boutique individual el volumen de datos normalmente puede ser manejado mediante bases de datos y herramientas convencionales.

Para determinar si realmente se trata de un problema de Big Data se pueden analizar características como volumen, velocidad, variedad y variabilidad. NIST señala que un problema de Big Data se relaciona con conjuntos extensos de datos que requieren arquitecturas escalables para su almacenamiento, procesamiento y análisis.

### Análisis de las V

| V | Situación en el hotel | Evaluación |
|---|---|---|
| **Volumen** | El hotel genera reservas, huéspedes y servicios, pero el volumen es limitado a escala individual. | **Bajo/medio** |
| **Velocidad** | Las reservas pueden llegar durante todo el día, pero no necesariamente a una velocidad masiva. | **Media** |
| **Variedad** | Existen datos estructurados, semiestructurados y textos de huéspedes. | **Media** |
| **Variabilidad** | La demanda puede cambiar según temporadas, fines de semana, eventos y vacaciones. | **Media/alta** |

Por lo tanto, el proyecto **no se considera Big Data** en su escala actual, aunque podría evolucionar hacia un escenario de Big Data si se integraran múltiples hoteles, plataformas de reservas, grandes cantidades de transacciones, datos en tiempo real y otras fuentes externas.

NIST relaciona Big Data con características como volumen, velocidad, variedad y variabilidad, especialmente cuando estas requieren una arquitectura escalable para procesar eficientemente los datos.

---

## 5. Ciclo de vida del proyecto

El ciclo de vida aplicado al proceso será:

**Pregunta → Obtener → Limpiar → Analizar → Visualizar → Decidir**

1. **Pregunta:** Definir qué se quiere conocer (*¿Cuál será la ocupación esperada durante las próximas semanas?*).
2. **Obtener:** Recolectar los datos provenientes del sistema de reservas, registros de huéspedes, cancelaciones, habitaciones y servicios.
3. **Limpiar:** Eliminar duplicados, corregir fechas incorrectas, tratar valores faltantes y estandarizar categorías como tipos de habitación y estados de reserva.
4. **Analizar:** Explorar los datos históricos para identificar patrones de ocupación, temporadas de alta demanda, cancelaciones y comportamiento de las reservas.
5. **Visualizar:** Crear gráficos y dashboards que permitan observar ocupación, cancelaciones y demanda por día/mes.
6. **Decidir:** Utilizar los resultados para tomar decisiones sobre disponibilidad de habitaciones y planificación de recursos.

### Flujo del proceso

* **1. PREGUNTA:** ¿Qué demanda se espera?
  ↓
* **2. OBTENER:** Reservas, huéspedes, cancelaciones...
  ↓
* **3. LIMPIAR:** Errores, duplicados, nulos...
  ↓
* **4. ANALIZAR:** Patrones y tendencias
  ↓
* **5. VISUALIZAR:** Gráficos y dashboards
  ↓
* **6. DECIDIR:** Planificar habitaciones y tarifas

## 6. Problem & Data
The selected process is the management of reservations and room occupancy in a boutique hotel. The main problem is the difficulty of understanding historical demand and anticipating future room occupancy. The data required includes reservation dates, check-in and check-out dates, room types, prices, reservation status, booking channels, cancellations, and additional services. Some data is structured, while other information, such as guest comments, can be unstructured or semi-structured. The main type of analytics is predictive analytics because the objective is to forecast future hotel occupancy using historical data. The project is not considered Big Data at its current scale because the volume and velocity of the data do not require a scalable Big Data architecture.

## 7. Conclusión
El diagnóstico permite identificar que la gestión de reservas de un hotel genera diferentes tipos de datos que pueden utilizarse para mejorar la toma de decisiones. El análisis descriptivo permite comprender el comportamiento histórico de la ocupación, mientras que la analítica predictiva permite anticipar la demanda futura. Aunque el proceso presenta variedad y variabilidad en sus datos, actualmente no alcanza necesariamente las características de un problema de Big Data debido a su volumen y velocidad moderados. La aplicación del ciclo de vida de datos permite transformar los registros obtenidos en información útil para la planificación y gestión del hotel.

## 8. Bibliografía
IBM. (2024). What is predictive analytics? IBM Think. https://www.ibm.com/topics/predictive-analytics

IBM. (2024). What is Big Data? IBM Think. https://www.ibm.com/topics/big-data

National Institute of Standards and Technology (NIST). (2019). NIST Big Data Interoperability Framework: Volume 1, Definitions. https://doi.org/10.6028/NIST.SP.1500-1r2

Amazon Web Services (AWS). (2026). What is Structured Data? https://aws.amazon.com/what-is/structured-data/

Amazon Web Services (AWS). (2026). Data Lake Foundation – Storage Best Practices for Data and Analytics Applications. https://aws.amazon.com/blogs/big-data/data-lake-foundation-storage-best-practices/
