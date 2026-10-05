# ERD — Tienda de ventas

```mermaid
erDiagram
    CATEGORIA ||--o{ PRODUCTO : "clasifica (1:N)"
    CLIENTE   ||--o{ PEDIDO   : "realiza (1:N)"
    PRODUCTO  ||--o{ PEDIDO   : "se vende en (1:N)"

    CATEGORIA {
        int categoria_id PK
        string nombre
    }
    PRODUCTO {
        int producto_id PK
        string nombre
        decimal precio
        int categoria_id FK
    }
    CLIENTE {
        int cliente_id PK
        string nombre
        string ciudad
    }
    PEDIDO {
        int id_pedido PK
        date fecha
        int cantidad
        string metodo_pago
        int cliente_id FK
        int producto_id FK
    }
```

**Cardinalidades:** una categoría tiene muchos productos (1:N); un cliente realiza muchos pedidos (1:N); un producto aparece en muchos pedidos (1:N). Cada pedido pertenece a un solo cliente y a un solo producto.
