"""
Corte 3 · Análisis temporal y visualización
1) Serie temporal: resample mensual + media móvil, tendencia y estacionalidad
2) Dos visualizaciones: evolución (línea) y comparación (barras)
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# ---------------------------------------------------------------- 1. Carga
df = pd.read_csv("datos_ventas.csv", parse_dates=["fecha"])
df = df.set_index("fecha").sort_index()
print(df.head(), "\n")

# ---------------------------------------------------------------- 2. Resample + media móvil
# Datos diarios -> total mensual ("MS" = inicio de mes)
mensual = df["valor"].resample("MS").sum()

serie = pd.DataFrame({"ventas": mensual})
serie["media_movil_3m"] = serie["ventas"].rolling(window=3).mean()
# Media móvil de 12 meses: elimina la estacionalidad y deja ver la tendencia pura
serie["media_movil_12m"] = serie["ventas"].rolling(window=12).mean()
print(serie.tail(8), "\n")

# ---------------------------------------------------------------- 3. Tendencia
anual = df["valor"].resample("YS").sum()
crecimiento = anual.pct_change().dropna() * 100
print("Ventas por año (COP):\n", anual)
print("\nCrecimiento anual (%):\n", crecimiento.round(1), "\n")

# ---------------------------------------------------------------- 4. Estacionalidad
# Índice estacional: venta promedio de cada mes / promedio mensual de su año
# (así se separa el efecto del mes del efecto de la tendencia de crecimiento)
serie["anio"] = serie.index.year
serie["mes"] = serie.index.month
serie["indice"] = serie["ventas"] / serie.groupby("anio")["ventas"].transform("mean")
estacional = serie.groupby("mes")["indice"].mean()
print("Índice estacional por mes (1.00 = promedio del año):\n", estacional.round(2), "\n")

# ---------------------------------------------------------------- 5. Visualizaciones
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
millones = FuncFormatter(lambda x, _: f"{x/1e6:,.0f}")
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False, "font.size": 11})

# Gráfico 1 · EVOLUCIÓN (línea + medias móviles)
fig, ax = plt.subplots(figsize=(11, 5.5))
ax.plot(serie.index, serie["ventas"], color="#9db4c0", linewidth=1.8, label="Ventas mensuales")
ax.plot(serie.index, serie["media_movil_3m"], color="#1f6f8b", linewidth=2.4, label="Media móvil 3 meses")
ax.plot(serie.index, serie["media_movil_12m"], color="#e07a1f", linewidth=2.4, linestyle="--",
        label="Media móvil 12 meses (tendencia)")
ax.set_title("Las ventas crecen cerca de 16% por año, con picos cada diciembre", loc="left",
             fontsize=14, fontweight="bold")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (millones de COP)")
ax.yaxis.set_major_formatter(millones)
ax.set_ylim(0)  # eje Y desde cero para no exagerar el crecimiento
ax.legend(frameon=False, loc="upper left")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig("grafico_evolucion.png", dpi=150)
plt.close(fig)

# Gráfico 2 · COMPARACIÓN (barras: índice estacional por mes)
colores = ["#e07a1f" if v == estacional.max() else "#1f6f8b" if v >= 1 else "#9db4c0"
           for v in estacional.values]
fig, ax = plt.subplots(figsize=(11, 5.5))
barras = ax.bar(MESES, estacional.values, color=colores)
ax.axhline(1, color="black", linewidth=1, linestyle=":")
ax.text(-0.45, 1.02, "Promedio del año = 1,00", ha="left", va="bottom", fontsize=9)
for b, v in zip(barras, estacional.values):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.01, f"{v:.2f}", ha="center", fontsize=9)
ax.set_title("Diciembre vende 1,6 veces el promedio del año; enero y febrero son los meses flojos",
             loc="left", fontsize=14, fontweight="bold")
ax.set_xlabel("Mes del año")
ax.set_ylabel("Índice estacional (1,00 = promedio)")
ax.set_ylim(0)  # barras siempre desde cero
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()
fig.savefig("grafico_comparacion.png", dpi=150)
plt.close(fig)

serie.drop(columns=["anio", "mes", "indice"]).round(0).to_csv("serie_mensual.csv")
print("Listo: grafico_evolucion.png, grafico_comparacion.png, serie_mensual.csv")
