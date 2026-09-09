# Actividad Evaluativa · Corte 1 (Parcial C1)

**Estudiante:** Álvaro Augusto Andrade Quesada  
**Usuario GitHub:** Tutolinis  
**Caso de Estudio:** Tienda en Línea de Tecnología (E-commerce)

---

## 1. Clasificación de Tipos de Datos

| Dato | Clasificación | Descripción |
| :--- | :--- | :--- |
| **Historial de transacciones y ventas** | Estructurado | Registro en base de datos relacional con columnas definidas (ID_Venta, Fecha, Monto, ID_Cliente). |
| **Registros del servidor de peticiones web (Logs HTTP)** | Semiestructurado | Archivos JSON o registros del servidor que contienen datos organizados pero dinámicos (IP, fecha, endpoint, navegador). |
| **Reseñas y comentarios de clientes** | No estructurado | Texto libre redactado por los usuarios en la plataforma sin un formato rígido predefinido. |
| **Imágenes de comprobantes de pago** | No estructurado | Archivos de imagen (PNG/JPG) subidos por los clientes para verificar transferencias bancarias. |

---

## 2. Preguntas de Analítica

* **Analítica Descriptiva:** ¿Cuál fue el producto más vendido y el volumen total de ingresos generados durante el último mes?
* **Analítica Predictiva:** ¿Cuántas unidades de cada producto se estiman vender durante la próxima temporada alta basándose en la tendencia histórica de compras?

---

## 3. Diagrama de Flujo de Datos

```text
[ Fuente ]                [ Almacenamiento ]             [ Análisis ]                  [ Visualización ]
Sistemas de ventas   ---> Base de datos PostgreSQL   ---> Consultas SQL y modelos  ---> Tableros interactivos
y registros web           y Amazon S3 (Archivos)        de aprendizaje automático    en Power BI / Metabase

` ``` `

4. Difference Between Descriptive and Predictive Analytics
Descriptive analytics focuses on summarizing historical data to explain what has already happened in the business.

Predictive analytics utilizes statistical models and historical trends to forecast future outcomes and behaviors.
