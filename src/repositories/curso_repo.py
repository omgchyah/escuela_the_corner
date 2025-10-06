from __future__ import annotations
from typing import Optional, List
from datetime import date, datetime

from src.database.db import get_connection
from src.models.curso import Curso

#Helper para normalizar nombre de curso

def _norm_nombre(s: str) -> str:
  return " ".join(s.strip().split()).title()

def _row_to_model(row: dict) -> Curso:
    # mysql-connector con dictionary=True devuelve date/datetime ya parseados
  return Curso(
        id=row["id"],
        nombre=row["nombre"],
        precio=float(row["precio"]),
        fecha_inicio=row.get("fecha_inicio"),
        fecha_fin=row.get("fecha_fin"),
        creado_en=row.get("creado_en"),
        actualizado_en=row.get("actualizado_en"),
    )
    
class CursoRepo:
  
  # ---------- CREATE ----------
  def crear_curso(self, curso: Curso) -> int:
    """
    Inserta un Curso y devuelve el id.
    """
    nombre = _norm_nombre(curso.nombre)
    precio = float(curso.precio)
    fi: Optional[date] = curso.fecha_inicio
    ff: Optional[date] = curso.fecha_fin

    conn = get_connection()
    cur = conn.cursor()
    try:
      sql = (f"INSERT INTO cursos"
                  f"(nombre, precio, fecha_inicio, fecha_fin) "
                  f"VALUES (%s, %s, %s, %s)")
      cur.execute(sql, (nombre, precio, fi, ff))
      conn.commit()
      return cur.lastrowid
    except Exception:
      conn.rollback()
      raise
    finally:
      cur.close()
      conn.close()

# ---------- READ ----------
  def buscar_por_id(self, curso_id: int) -> Optional[Curso]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
      sql = f"SELECT * FROM cursos WHERE id = %s"
      cur.execute(sql, (curso_id,))
      row = cur.fetchone()
      return _row_to_model(row) if row else None
    finally:
      cur.close()
      conn.close()
  
  def listar_por_precio(self) -> List[Curso]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
      cur.execute(f"SELECT * FROM cursos ORDER BY precio ASC")
      return [_row_to_model(r) for r in cur.fetchall()]
    finally:
      cur.close()
      conn.close()

  def buscar_todos(self) -> List[Curso]:
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    try:
      cur.execute(f"SELECT * FROM cursos ORDER BY id")
      return [_row_to_model(r) for r in cur.fetchall()]
    finally:
      cur.close()
      conn.close()
      
  # ---------- UPDATE ----------          
  def actualizar_precio_por_id(self, curso_id: int, nuevo_precio: float) -> bool:
    """
    Actualiza únicamente el precio del curso.
    Devuelve True si afectó a 1 fila, False si no existía el id.
    """
    try:
      precio = round(float(nuevo_precio), 2)
    except (TypeError, ValueError):
      raise ValueError("Nuevo precio debe ser numérico.")

    if precio < 0:
      raise ValueError("Nuevo precio no puede ser negativo.")

    conn = get_connection()
    cur = conn.cursor()
    try:
      sql = f"UPDATE cursos SET precio = %s WHERE id = %s"
      cur.execute(sql, (precio, curso_id))
      conn.commit()
      return cur.rowcount == 1
    except Exception:
      conn.rollback()
      raise
    finally:
      cur.close()
      conn.close()
          
  # ---------- DELETE ----------
  def borrar_por_id(self, curso_id: int) -> bool:
    conn = get_connection()
    cur = conn.cursor()
    try:
        sql = f"DELETE FROM cursos WHERE id = %s"
        cur.execute(sql, (curso_id,))
        conn.commit()
        return cur.rowcount == 1
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()
        

# ###Ejemplo
# curso_repo = CursoRepo()
        
# def demo_create_with_model():
#     curso = Curso(
#         nombre="python intensivo",
#         precio=199.99,
#         fecha_inicio=date(2025, 10, 20),
#         fecha_fin=date(2025, 11, 20),
#     )
#     new_id = curso_repo.crear_curso(curso)
#     print(f"✅ Creado curso id={new_id}")

# def demo_list_all():
#     cursos = curso_repo.buscar_todos()
#     if not cursos:
#         print("ℹ️ No hay cursos aún.")
#         return
#     print("📚 Lista de cursos:")
#     for c in cursos:
#         print("-" * 40)
#         print(c.info(), end="")

# def demo_get_by_id(curso_id: int):
#     c = curso_repo.buscar_por_id(curso_id)
#     if c:
#         print("📄 Curso encontrado:\n" + c.info())
#     else:
#         print(f"⚠️ No existe curso id={curso_id}")
        

# def demo_delete(curso_id: int):
#     ok = curso_repo.borrar_por_id(curso_id)
#     print("🗑️ Eliminado" if ok else f"⚠️ No existe id={curso_id}")
    
# ok = curso_repo.actualizar_precio_por_id(1, 249.90)
# print("✅ Precio actualizado" if ok else "⚠️ No existe ese id")
        
        
        
# demo_create_with_model()
# demo_list_all()
# demo_get_by_id(1)
# demo_delete(2)
        
