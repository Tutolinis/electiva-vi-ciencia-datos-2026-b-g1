"""
Corte 3 · Optimización de una consulta SQL (antes vs. después)

Se crea una tabla `ventas` en SQLite con 1.000.000 de filas (tomando como base las
fechas, productos y precios del dataset) para que la diferencia de rendimiento sea medible.
"""
import sqlite3
import time
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
N = 1_000_000

# ------------------------------------------------------------ Tabla grande de prueba
base = pd.read_csv("datos_ventas.csv", parse_dates=["fecha"])
fechas = pd.date_range("2023-01-01", "2025-12-31", freq="D")
productos = base["producto"].unique()

ventas = pd.DataFrame({
    "id": np.arange(1, N + 1),
    "fecha": rng.choice(fechas, N).astype("datetime64[D]").astype(str),
    "producto": rng.choice(productos, N),
    "cliente": rng.integers(1, 5000, N),
    "unidades": rng.integers(1, 10, N),
    "valor": rng.integers(20_000, 400_000, N),
    "notas": "texto de relleno para simular columnas que no se necesitan " * 2,
})

con = sqlite3.connect(":memory:")
ventas.to_sql("ventas", con, index=False)
print(f"Tabla 'ventas' creada con {N:,} filas\n")


def medir(sql, repeticiones=5):
    """Ejecuta la consulta varias veces y devuelve (mejor tiempo en ms, filas)."""
    tiempos = []
    for _ in range(repeticiones):
        t0 = time.perf_counter()
        filas = con.execute(sql).fetchall()
        tiempos.append((time.perf_counter() - t0) * 1000)
    return min(tiempos), len(filas)


def plan(sql):
    return [r[3] for r in con.execute("EXPLAIN QUERY PLAN " + sql)]


# ------------------------------------------------------------ ANTES (consulta lenta)
ANTES = """
SELECT *
FROM ventas
WHERE strftime('%Y', fecha) = '2025' AND strftime('%m', fecha) = '03'
"""

# ------------------------------------------------------------ DESPUÉS (consulta optimizada)
INDICE = "CREATE INDEX idx_ventas_fecha ON ventas(fecha)"
DESPUES = """
SELECT fecha, producto, unidades, valor
FROM ventas
WHERE fecha >= '2025-03-01' AND fecha < '2025-04-01'
"""

t_antes, n_antes = medir(ANTES)
print("ANTES")
print("  Plan   :", plan(ANTES))
print(f"  Tiempo : {t_antes:,.1f} ms  ({n_antes:,} filas)\n")

con.execute(INDICE)
con.commit()

t_despues, n_despues = medir(DESPUES)
print("DESPUÉS")
print("  Plan   :", plan(DESPUES))
print(f"  Tiempo : {t_despues:,.1f} ms  ({n_despues:,} filas)\n")

assert n_antes == n_despues, "Las dos consultas deben devolver las mismas filas"
print(f"Mejora: {t_antes / t_despues:,.1f}x más rápida ({(1 - t_despues / t_antes) * 100:.0f}% menos tiempo)")
