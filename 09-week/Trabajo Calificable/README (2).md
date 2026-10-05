# Corte 2 — Modelo, consulta y limpieza de datos

**Nombre:** NOMBRE COMPLETO · **GitHub:** USUARIO

## Contenido
- `erd.md` — diagrama entidad-relación (4 entidades, cardinalidades 1:N).
- `generar_dataset.py` — genera `ventas_raw.csv` (dataset sucio de una tienda, 530 filas).
- `limpieza_ventas.ipynb` — limpieza con pandas, comparación antes/después y 2 consultas.
- `ventas_raw.csv` / `ventas_clean.csv` — datos originales y limpios.

## Data & cleaning
This project uses a dataset of 530 store orders from January to September 2026, with columns such as date, customer, city, product, category, price, quantity and payment method. The raw data had 186 null values, 30 duplicate rows, prices stored as text with "$" and commas, mixed date formats, invalid negative quantities and inconsistent text (extra spaces and different capitalization). I removed the duplicates, converted prices and dates to proper types, normalized the text columns, and imputed missing values using the most frequent value per product or customer, the median for quantity and "Desconocido" for payment method. After cleaning, the dataset has 500 rows and no nulls. The first question showed that Technology is the top category between June and September, with about 77% of revenue. The second question, answered with SQL, showed that Cali has the highest average ticket among card payments, at about 1,995,500 COP.
