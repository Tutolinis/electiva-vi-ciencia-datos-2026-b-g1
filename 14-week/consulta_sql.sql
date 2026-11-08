-- =====================================================================
-- Corte 3 · Optimización de consulta SQL (ventas de marzo de 2025)
-- =====================================================================

-- ANTES (lenta) -------------------------------------------------------
-- Problemas: SELECT * trae columnas innecesarias y la función sobre la
-- columna `fecha` en el WHERE impide usar un índice (escaneo completo).
SELECT *
FROM ventas
WHERE strftime('%Y', fecha) = '2025'
  AND strftime('%m', fecha) = '03';

-- DESPUÉS (optimizada) ------------------------------------------------
-- 1) Índice sobre la columna de filtro
CREATE INDEX idx_ventas_fecha ON ventas(fecha);

-- 2) Solo las columnas necesarias + filtro por rango (sin función en el WHERE)
SELECT fecha, producto, unidades, valor
FROM ventas
WHERE fecha >= '2025-03-01'
  AND fecha <  '2025-04-01';

-- Nota: en MySQL/SQL Server el "antes" equivale a WHERE YEAR(fecha)=2025 AND MONTH(fecha)=3
