"""Genera ventas_raw.csv: dataset 'sucio' de una tienda (con nulos, duplicados, tipos y formatos inconsistentes)."""
import numpy as np, pandas as pd
rng = np.random.default_rng(42)
N = 500
productos = {"Laptop":("Tecnologia",2500000),"Mouse":("Tecnologia",45000),"Teclado":("Tecnologia",120000),
             "Audifonos":("Tecnologia",180000),"Camiseta":("Ropa",55000),"Jean":("Ropa",130000),
             "Zapatos":("Ropa",210000),"Cafetera":("Hogar",260000),"Licuadora":("Hogar",190000),"Lampara":("Hogar",85000)}
clientes = {i:(n,c) for i,(n,c) in enumerate(zip(
    ["Ana Torres","Luis Perez","Maria Gomez","Carlos Ruiz","Sofia Diaz","Juan Mora","Laura Rojas","Andres Vega","Paula Leon","Diego Castro"],
    ["Neiva","Bogota","Medellin","Cali","Neiva","Bogota","Pitalito","Neiva","Medellin","Cali"]),start=1)}
nombres = list(productos)
rows=[]
for i in range(1,N+1):
    p = rng.choice(nombres); cid = int(rng.integers(1,11)); nom,ciu = clientes[cid]
    rows.append({"id_pedido":i,"fecha":(pd.Timestamp("2026-01-01")+pd.Timedelta(days=int(rng.integers(0,270)))),
        "cliente_id":cid,"cliente_nombre":nom,"ciudad":ciu,"producto":p,"categoria":productos[p][0],
        "precio":productos[p][1],"cantidad":int(rng.integers(1,6)),
        "metodo_pago":rng.choice(["Tarjeta","Efectivo","Transferencia"])})
df = pd.DataFrame(rows)
# --- ensuciar ---
df["fecha"] = df["fecha"].dt.strftime("%Y-%m-%d")
idx = rng.choice(N, 80, replace=False); df.loc[idx,"fecha"] = pd.to_datetime(df.loc[idx,"fecha"]).dt.strftime("%d/%m/%Y")
df["precio"] = df["precio"].astype(object); df["cantidad"]=df["cantidad"].astype(object)
idx = rng.choice(N, 60, replace=False); df.loc[idx,"precio"] = df.loc[idx,"precio"].apply(lambda x: f"${x:,}")
for col,k in [("ciudad",40),("metodo_pago",35),("categoria",30),("cantidad",25),("precio",25),("cliente_nombre",20)]:
    df.loc[rng.choice(N,k,replace=False),col] = np.nan
idx = rng.choice(N,60,replace=False); df.loc[idx,"ciudad"] = df.loc[idx,"ciudad"].astype(str).str.upper().replace("NAN",np.nan)
idx = rng.choice(N,50,replace=False); df.loc[idx,"producto"] = " "+df.loc[idx,"producto"].str.lower()+"  "
idx = rng.choice(N,30,replace=False); df.loc[idx,"metodo_pago"] = df.loc[idx,"metodo_pago"].astype(str).str.lower().replace("nan",np.nan)
df.loc[rng.choice(N,5,replace=False),"cantidad"] = -1
df = pd.concat([df, df.sample(30, random_state=1)], ignore_index=True).sample(frac=1, random_state=7).reset_index(drop=True)
df.to_csv("ventas_raw.csv", index=False)
print(df.shape)
