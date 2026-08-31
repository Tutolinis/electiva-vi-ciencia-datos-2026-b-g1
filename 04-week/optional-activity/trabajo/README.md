Diagnóstico de datos de un proceso
1. Problema y pregunta de datos

Proceso seleccionado: Gestión de reservas y ocupación de un hotel boutique.

Problema

Un hotel boutique necesita gestionar adecuadamente sus reservas y conocer con anticipación la demanda de habitaciones. Cuando la información de reservas, cancelaciones, huéspedes y servicios se encuentra dispersa, puede ser difícil identificar patrones de ocupación y tomar decisiones oportunas sobre disponibilidad y recursos.

El objetivo del análisis es utilizar los datos históricos de las reservas para comprender el comportamiento de la demanda y anticipar la ocupación futura del hotel.

Pregunta de datos

¿Cuál será la ocupación esperada del hotel durante las próximas semanas y qué patrones históricos de reservas pueden ayudar a anticipar la demanda de habitaciones?

Esta pregunta permite utilizar información histórica para realizar una analítica predictiva, ya que busca estimar un comportamiento futuro a partir de datos anteriores. La analítica predictiva utiliza datos históricos y patrones anteriores para realizar pronósticos sobre resultados futuros.

## 2. Data Inventory

To answer the data question, the project requires information from different sources related to the hotel's reservation process.

### Structured Data

- **Reservation ID:** Unique identifier for each reservation.
- **Reservation date:** Date when the reservation was created.
- **Check-in date:** Date when the guest arrives at the hotel.
- **Check-out date:** Date when the guest leaves the hotel.
- **Room type:** Single, double, suite, etc.
- **Room rate:** Price charged per night.
- **Reservation status:** Confirmed, cancelled, completed, etc.
- **Additional services:** Spa, restaurant, laundry, and other services consumed.

### Semi-Structured Data

- **Booking channel:** Website, phone, external platform, travel agency, etc.
- **External platform records:** Reservation information received through formats such as JSON.

### Unstructured Data

- **Guest comments:** Opinions, observations, and feedback written by customers.
- **Attached documents:** Additional files or documents related to reservations.

### Data Classification

```mermaid
flowchart LR
    A["DATA INVENTORY"]

    A --> B["STRUCTURED"]
    A --> C["SEMI-STRUCTURED"]
    A --> D["UNSTRUCTURED"]

    B --> B1["Reservation ID"]
    B --> B2["Reservation dates"]
    B --> B3["Room type"]
    B --> B4["Room rate"]
    B --> B5["Reservation status"]
    B --> B6["Additional services"]

    C --> C1["Booking channel"]
    C --> C2["External platform records"]

    D --> D1["Guest comments"]
    D --> D2["Attached documents"]
3. Tipo de analítica
Analítica predictiva

El tipo de analítica principal que se aplicará es predictiva.

La razón es que el objetivo no solamente es conocer qué ocurrió con las reservas anteriores, sino utilizar esos datos para estimar la ocupación futura del hotel.

Por ejemplo, a partir de variables como:

Reservas históricas.
Fechas de entrada y salida.
Temporada.
Día de la semana.
Tipo de habitación.
Cancelaciones.
Canal de reserva.
Número de huéspedes.

se podría construir un modelo que estime la cantidad de habitaciones que probablemente estarán ocupadas en un período futuro.

La analítica predictiva busca precisamente utilizar datos históricos y actuales para anticipar tendencias o resultados futuros.

Analítica descriptiva como etapa previa

Antes de realizar la predicción también se utilizaría analítica descriptiva para responder preguntas como:

¿Cuántas habitaciones se ocuparon durante los últimos meses?

¿Cuál fue el porcentaje promedio de ocupación?

¿Qué días tuvieron mayor demanda?

Esto permite comprender el comportamiento histórico antes de construir una predicción.

La analítica descriptiva responde principalmente qué ocurrió, mientras que la predictiva busca estimar qué podría ocurrir posteriormente.

```markdown
## 4. Is this a Big Data case?

### Current Situation

The project is **not considered a Big Data case at its current scale**.

The hotel generates different types of information and the amount of data can increase over time. However, a single boutique hotel would normally have a moderate volume and processing speed that can be handled using conventional database technologies.

### Big Data Analysis

The project can be evaluated using the main characteristics of Big Data:

```mermaid
mindmap
  root((BIG DATA))
    Volume
      Moderate amount of reservations
      Limited to one hotel
    Velocity
      Reservations arrive throughout the day
      No massive real-time data flow
    Variety
      Structured data
      Semi-structured data
      Unstructured text
    Variability
      Seasonal demand
      Weekends
      Holidays
      Special events
## 5. Data Life Cycle

The data life cycle applied to the hotel reservation process is:

**1. Question → 2. Obtain → 3. Clean → 4. Analyze → 5. Visualize → 6. Decide**

| Step | Description |
|---|---|
| **1. Question** | Define the data question: What will the expected hotel occupancy be in the coming weeks? |
| **2. Obtain** | Collect reservation, guest, room, cancellation, and service data. |
| **3. Clean** | Remove duplicates, correct errors, handle missing values, and standardize the data. |
| **4. Analyze** | Identify historical occupancy patterns, demand trends, and cancellations. |
| **5. Visualize** | Create charts and dashboards to represent occupancy and demand. |
| **6. Decide** | Use the results to plan room availability and hotel resources. |

### Data Life Cycle Diagram

```text
┌───────────────┐
│   QUESTION    │
│ Define the    │
│ data problem  │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│    OBTAIN     │
│ Collect the   │
│ required data │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│     CLEAN     │
│ Prepare and   │
│ validate data │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│    ANALYZE    │
│ Find patterns │
│ and trends    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  VISUALIZE    │
│ Charts and    │
│ dashboards    │
└───────┬───────┘
        │
        ▼
┌───────────────┐
│    DECIDE     │
│ Make informed │
│ decisions     │
└───────────────┘
6. Problem & Data

Esta sección debe estar en inglés, porque el profesor especifica mínimo 5 oraciones.

Problem & Data

The selected process is the management of reservations and room occupancy in a boutique hotel. The main problem is the difficulty of understanding historical demand and anticipating future room occupancy. The data required includes reservation dates, check-in and check-out dates, room types, prices, reservation status, booking channels, cancellations, and additional services. Some data is structured, while other information, such as guest comments, can be unstructured or semi-structured. The main type of analytics is predictive analytics because the objective is to forecast future hotel occupancy using historical data. The project is not considered Big Data at its current scale because the volume and velocity of the data do not require a scalable Big Data architecture.


7. Conclusión

El diagnóstico permite identificar que la gestión de reservas de un hotel genera diferentes tipos de datos que pueden utilizarse para mejorar la toma de decisiones. El análisis descriptivo permite comprender el comportamiento histórico de la ocupación, mientras que la analítica predictiva permite anticipar la demanda futura. Aunque el proceso presenta variedad y variabilidad en sus datos, actualmente no alcanza necesariamente las características de un problema de Big Data debido a su volumen y velocidad moderados. La aplicación del ciclo de vida de datos permite transformar los registros obtenidos en información útil para la planificación y gestión del hotel.

8. Bibliografía


IBM. (2024). What is predictive analytics? IBM Think. IBM – What is Predictive Analytics?
IBM. (2024). What is Big Data? IBM Think. IBM – What is Big Data?
National Institute of Standards and Technology (NIST). (2019). NIST Big Data Interoperability Framework: Volume 1, Definitions. NIST – Big Data Interoperability Framework
Amazon Web Services (AWS). (2026). What is Structured Data? AWS – What is Structured Data?
Amazon Web Services (AWS). (2026). Data Lake Foundation – Storage Best Practices for Data and Analytics Applications. AWS – Data Lake Foundation
