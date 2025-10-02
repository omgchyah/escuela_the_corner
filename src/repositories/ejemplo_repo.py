#1) Importar db.py
from src.database.db import get_connection

#2) Crear la conexión
conn = get_connection()  # usa .env automáticamente

#3) Crear el cursor
# Si quieres filas como diccionarios (más cómodo para imprimir):
cur = conn.cursor(dictionary=True)
# Si te valen tuplas:
# cur = conn.cursor()

#4) Ejecutar la query (ejemplos)
cur.execute(
    "INSERT INTO cursos (nombre, precio) VALUES (%s, %s)",
    ("Python Básico", 120.00)
)

cur.execute(
    "UPDATE cursos SET precio = %s WHERE id = %s",
    (150.00, 1)
)

cur.execute(
    "DELETE FROM cursos WHERE id = %s",
    (1,)
)

cur.execute("SELECT id, nombre, precio FROM cursos ORDER BY id")
filas = cur.fetchall()
for fila in filas:
    print(fila)  # si dictionary=True verás {'id':..., 'nombre':..., 'precio':...}
    
# INSERT
cur.execute("INSERT INTO estudiantes (nombre, edad, dni) VALUES (%s, %s, %s)", ("Laura", 19, "Z1234567X"))

# UPDATE
cur.execute("UPDATE estudiantes SET nombre=%s WHERE id=%s", ("Laura Gómez", 2))

# DELETE
cur.execute("DELETE FROM estudiantes WHERE id=%s", (2,))

# SELECT
cur.execute("SELECT id, nombre, edad FROM estudiantes ORDER BY id")
print(cur.fetchall())

#5) Commit
#En nuestro db.py el autocommit=True ya está activado, así que normalmente no necesitas conn.commit().
#Si tuvieras autocommit=False (otro proyecto), entonces:
conn.commit()

#6) Imprimir la tabla (ya lo hicimos en el SELECT)
# 'filas' ya tiene los registros. Puedes volver a listar después de un INSERT/UPDATE/DELETE

#7) Cerrar cursor y conexión (siempre)
cur.close()
conn.close()


##########################################################################################

# EJEMPLO DE REPOSITORY

##########################################################################################

# src/repositories/repo_item.py
# Repositorio de ejemplo para la tabla 'items'
# Tabla esperada:
# CREATE TABLE items (
#   id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
#   nombre VARCHAR(50) NOT NULL,
#   precio DECIMAL(10,2) NOT NULL DEFAULT 0.00,
#   creado_en TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# ) ENGINE=InnoDB;

# from src.database.db import get_connection

# class RepoItem:
#     TABLE = "items"

#     # CREATE
#     def create(self, nombre: str, precio: float) -> int:
#         conn = get_connection()                 # 1) conexión
#         cur = conn.cursor()                      # 2) cursor
#         try:
#             sql = f"INSERT INTO {self.TABLE} (nombre, precio) VALUES (%s, %s)"
#             cur.execute(sql, (nombre, precio))  # 3) execute
#             conn.commit()                       # 4) commit
#             nuevo_id = cur.lastrowid
#             return nuevo_id
#         except Exception:
#             conn.rollback()                     # si algo falla, revierte
#             raise
#         finally:
#             cur.close()                         # 6) cerrar cursor
#             conn.close()                        # 7) cerrar conexión

#     # READ (por id)
#     def get_by_id(self, item_id: int):
#         conn = get_connection()
#         cur = conn.cursor(dictionary=True)
#         try:
#             sql = f"SELECT id, nombre, precio FROM {self.TABLE} WHERE id = %s"
#             cur.execute(sql, (item_id,))
#             fila = cur.fetchone()               # 4) execute+fetch
#             return fila                          # dict o None
#         finally:
#             cur.close()
#             conn.close()

#     # LIST (todos)
#     def list_all(self):
#         conn = get_connection()
#         cur = conn.cursor(dictionary=True)
#         try:
#             sql = f"SELECT id, nombre, precio FROM {self.TABLE} ORDER BY id"
#             cur.execute(sql)
#             filas = cur.fetchall()
#             return filas
#         finally:
#             cur.close()
#             conn.close()

#     # UPDATE (solo nombre en este ejemplo)
#     def update_nombre(self, item_id: int, nuevo_nombre: str) -> bool:
#         conn = get_connection()
#         cur = conn.cursor()
#         try:
#             sql = f"UPDATE {self.TABLE} SET nombre = %s WHERE id = %s"
#             cur.execute(sql, (nuevo_nombre, item_id))
#             conn.commit()
#             return cur.rowcount == 1
#         except Exception:
#             conn.rollback()
#             raise
#         finally:
#             cur.close()
#             conn.close()

#     # UPDATE (precio, ejemplo adicional)
#     def update_precio(self, item_id: int, nuevo_precio: float) -> bool:
#         conn = get_connection()
#         cur = conn.cursor()
#         try:
#             sql = f"UPDATE {self.TABLE} SET precio = %s WHERE id = %s"
#             cur.execute(sql, (nuevo_precio, item_id))
#             conn.commit()
#             return cur.rowcount == 1
#         except Exception:
#             conn.rollback()
#             raise
#         finally:
#             cur.close()
#             conn.close()

#     # DELETE
#     def delete(self, item_id: int) -> bool:
#         conn = get_connection()
#         cur = conn.cursor()
#         try:
#             sql = f"DELETE FROM {self.TABLE} WHERE id = %s"
#             cur.execute(sql, (item_id,))
#             conn.commit()
#             return cur.rowcount == 1
#         except Exception:
#             conn.rollback()
#             raise
#         finally:
#             cur.close()
#             conn.close()

#     # SEARCH (por nombre, coincidencia parcial)
#     def find_by_name(self, texto: str):
#         conn = get_connection()
#         cur = conn.cursor(dictionary=True)
#         try:
#             sql = f"SELECT id, nombre, precio FROM {self.TABLE} WHERE nombre LIKE %s ORDER BY nombre"
#             cur.execute(sql, (f"%{texto}%",))
#             filas = cur.fetchall()
#             return filas
#         finally:
#             cur.close()
#             conn.close()
