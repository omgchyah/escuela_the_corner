# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import Optional, List, Dict, Any
from src.database.db import get_connection

def _norm_nombre(s: str) -> str:
    return " ".join(s.strip().split()).title()

def _norm_dni(s: str) -> str:
    return s.replace(" ", "").upper()

class AlumnoRepo:
    TABLE = "alumnos"

    # --------- CREATE ----------
    def crear_alumno(self, nombre: str, edad: Optional[int], dni: str,
                    telefono: Optional[str] = None,
                    direccion: Optional[str] = None) -> int:
        nombre = _norm_nombre(nombre)
        dni = _norm_dni(dni)

        if edad is not None:
            try:
                edad = int(edad)
                if not (0 <= edad <= 120):
                    raise ValueError("edad fuera de rango razonable (0-120).")
            except (TypeError, ValueError):
                raise ValueError("edad debe ser un entero o None.")

        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = (f"INSERT INTO {self.TABLE} "
                f"(nombre, edad, dni, telefono, direccion) "
                f"VALUES (%s, %s, %s, %s, %s)")
            cur.execute(sql, (nombre, edad, dni, telefono, direccion))
            conn.commit()
            return cur.lastrowid
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

    # --------- READ ----------
    def buscar_por_id(self, alumno_id: int) -> Optional[Dict[str, Any]]:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (f"SELECT id, nombre, edad, dni, telefono, direccion, "
                f"creado_en, actualizado_en FROM {self.TABLE} WHERE id = %s")
            cur.execute(sql, (alumno_id,))
            return cur.fetchone()
        finally:
            cur.close()
            conn.close()

    def buscar_por_nombre(self, texto: str) -> List[Dict[str, Any]]:
        patron = f"%{' '.join(texto.strip().split())}%"
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (f"SELECT id, nombre, edad, dni, telefono, direccion, "
                f"creado_en, actualizado_en FROM {self.TABLE} "
                f"WHERE nombre LIKE %s ORDER BY nombre")
            cur.execute(sql, (patron,))
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    # --------- LIST ----------
    def mostrar_todos(self) -> List[Dict[str, Any]]:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (f"SELECT id, nombre, edad, dni, telefono, direccion, "
                f"creado_en, actualizado_en FROM {self.TABLE} ORDER BY id")
            cur.execute(sql)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    # --------- UPDATE ----------
    def actualizar_nombre_por_id(self, alumno_id: int, nuevo_nombre: str) -> bool:
        nuevo_nombre = _norm_nombre(nuevo_nombre)
        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = f"UPDATE {self.TABLE} SET nombre = %s WHERE id = %s"
            cur.execute(sql, (nuevo_nombre, alumno_id))
            conn.commit()
            return cur.rowcount == 1
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

    # (Opcional) Actualizar DNI
    def actualizar_dni_por_id(self, alumno_id: int, nuevo_dni: str) -> bool:
        nuevo_dni = _norm_dni(nuevo_dni)
        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = f"UPDATE {self.TABLE} SET dni = %s WHERE id = %s"
            cur.execute(sql, (nuevo_dni, alumno_id))
            conn.commit()
            return cur.rowcount == 1
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

        # --------- DELETE ----------
    def borrar_por_id(self, alumno_id: int) -> bool:
        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = f"DELETE FROM {self.TABLE} WHERE id = %s"
            cur.execute(sql, (alumno_id,))
            conn.commit()
            return cur.rowcount == 1
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
            
# =======================
# Ejemplos de uso rápido
# =======================
# if __name__ == "__main__":
#     repo = AlumnoRepo()

#     # Crear
#     nuevo_id = repo.crear_alumno(
#         nombre="  maria   lopez ",
#         edad=54,
#         dni="15844962p",
#         telefono="600123123",
#         direccion="C/ Mayor 123"
#     )
#     print("✅ Creado id:", nuevo_id)

#     # Leer
#     print("📄 Alumno:", repo.buscar_por_id(nuevo_id))

#     # Actualizar nombre
#     print("✏️ Nombre OK:", repo.actualizar_nombre_por_id(nuevo_id, "maria del mar lópez"))

#     # Actualizar DNI
#     print("🆔 DNI OK:", repo.actualizar_dni_por_id(nuevo_id, "15844962P"))

#     # Listar
#     print("📚 Total:", len(repo.mostrar_todos()))

#     # Buscar por nombre
#     print("🔎 Encontrados:", len(repo.buscar_por_nombre("maria")))

#     # Borrar
#     print("🗑️ Borrado:", repo.borrar_por_id(nuevo_id))

