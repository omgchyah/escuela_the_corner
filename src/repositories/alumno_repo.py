# Repositorio completado
from src.database.db import get_connection

conn = get_connection()  # usa .env automáticamente

cur = conn.cursor(dictionary=True)

cur.execute(
    "INSERT INTO alumnos (nombre, edad, dni) VALUES (%s, %s, %s)",
    ("María", 54, "15844962P")
)

conn.commit()

cur.close()
conn.close()

# CREATE (Crear)
def crear_alumno(self, nombre, edad, dni, telefono, direccion):
    conn = get_connection()
    cur = conn.cursor()
    try:
            sql = f"INSERT INTO {self.TABLE} (nombre, edad, dni, direccion) VALUES (%s, %s)"
            cur.execute(sql, (nombre, edad, dni, telefono, direccion))
            conn.commit()
            nuevo_id = cur.lastrowid
            return nuevo_id
    except Exception:
            conn.rollback()
            raise
    finally:
            cur.close()
            conn.close()
            
# READ (Leer)
def get_by_id(self, item_id: int):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        sql = f"SELECT id, nombre, edad, dni, telefono, direccion FROM {self.TABLE} WHERE id = %s"
        cur.execute(sql, (item_id,))
        fila = cur.fetchone()
        return fila
    finally:
        cur.close()
        conn.close()
            
# LIST
def list_all(self):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        sql = f"SELECT id, nombre, edad, dni, telefono, direccion FROM {self.TABLE} ORDER BY id"
        cur.execute(sql)
        filas = cur.fetchall()
        return filas
    finally:
        cur.close()
        conn.close()
            
# UPDATE
def update_nombre(self, item_id: int, nuevo_nombre: str) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"UPDATE {self.TABLE} SET nombre = %s WHERE id = %s"
        cur.execute(sql, (nuevo_nombre, item_id))
        conn.commit()
        return cur.rowcount == 1
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
            
# UPDATE
def update_precio(self, item_id: int, nuevo_id) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"UPDATE {self.TABLE} SET id = %s WHERE id = %s"
        cur.execute(sql, (nuevo_id, item_id))
        conn.commit()
        return cur.rowcount == 1
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
            
# DELETE (Eliminar)
def delete(self, item_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"DELETE FROM {self.TABLE} WHERE id = %s"
        cur.execute(sql, (item_id,))
        conn.commit()
        return cur.rowcount == 1
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

# SEARCH (Buscar)
def find_by_name(self, texto: str):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
        sql = f"SELECT id, nombre, edad, dni, telefono, direccion FROM {self.TABLE} WHERE nombre LIKE %s ORDER BY nombre"
        cur.execute(sql, (f"%{texto}%",))
        filas = cur.fetchall()
        return filas
    finally:
        cur.close()
        conn.close()