"""
Genera un dataset sintético de ventas diarias de una tienda (2023-01-01 a 2025-12-31).

Si tienes el dataset de ventas de la actividad del Corte 2, puedes reemplazar
`datos_ventas.csv` por el tuyo (columnas: fecha, producto, unidades, valor).
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)  # semilla fija -> resultados reproducibles

fechas = pd.date_range("2023-01-01", "2025-12-31", freq="D")
productos = {"Camisetas": 35_000, "Jeans": 90_000, "Zapatos": 140_000, "Accesorios": 25_000}

# Estacionalidad mensual (índice multiplicativo): picos en junio (Día del Padre/mitad de año)
# y diciembre (Navidad); valle en enero y febrero.
estacionalidad = {1: 0.80, 2: 0.85, 3: 0.95, 4: 0.95, 5: 1.05, 6: 1.20,
                  7: 1.00, 8: 0.95, 9: 0.95, 10: 1.00, 11: 1.15, 12: 1.45}

filas = []
for dia_idx, fecha in enumerate(fechas):
    tendencia = 1 + 0.0005 * dia_idx            # crecimiento sostenido (~+55% en 3 años)
    fin_de_semana = 1.25 if fecha.dayofweek >= 4 else 1.0   # viernes-domingo venden más
    for producto, precio in productos.items():
        base = 6 * tendencia * estacionalidad[fecha.month] * fin_de_semana
        unidades = rng.poisson(base)
        if unidades == 0:
            continue
        valor = unidades * precio * rng.normal(1.0, 0.03)
        filas.append((fecha.date(), producto, int(unidades), round(valor)))

df = pd.DataFrame(filas, columns=["fecha", "producto", "unidades", "valor"])
df.to_csv("datos_ventas.csv", index=False)
print(f"datos_ventas.csv generado: {len(df):,} filas")
print(df.head())
