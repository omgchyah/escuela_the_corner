# -*- coding: utf-8 -*-
from __future__ import annotations
from typing import List, Dict, Any, Optional
from src.database.db import get_connection

class AlumnoCursoRepo:
    TABLE = "alumno_curso"

    # --------- CREATE / UPSERT ----------
    def inscribir(self, id_alumno: int, id_curso: int) -> bool:
        """
        Inserta la matrícula. Devuelve True si creó, False si ya existía.
        Usa INSERT IGNORE para no romper por PK duplicada.
        """
        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = f"INSERT IGNORE INTO {self.TABLE} (id_alumno, id_curso) VALUES (%s, %s)"
            cur.execute(sql, (id_alumno, id_curso))
            conn.commit()
            return cur.rowcount == 1  # 1=creada, 0=ya existía
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()

    # --------- READ ----------
    def listar_cursos_de_alumno(self, id_alumno: int) -> List[Dict[str, Any]]:
        """
        Devuelve cursos (con nombre/precio/fechas) donde está matriculado el alumno.
        """
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (
                "SELECT ac.id_curso, ac.matriculado_en, "
                "       c.nombre AS curso_nombre, c.precio, c.fecha_inicio, c.fecha_fin "
                f"FROM {self.TABLE} ac "
                "JOIN cursos c ON c.id = ac.id_curso "
                "WHERE ac.id_alumno = %s "
                "ORDER BY ac.matriculado_en DESC, ac.id_curso"
            )
            cur.execute(sql, (id_alumno,))
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    def listar_alumnos_de_curso(self, id_curso: int) -> List[Dict[str, Any]]:
        """
        Devuelve alumnos (con nombre/dni/telefono) matriculados en el curso.
        """
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (
                "SELECT ac.id_alumno, ac.matriculado_en, "
                "       a.nombre AS alumno_nombre, a.dni, a.telefono "
                f"FROM {self.TABLE} ac "
                "JOIN alumnos a ON a.id = ac.id_alumno "
                "WHERE ac.id_curso = %s "
                "ORDER BY ac.matriculado_en DESC, ac.id_alumno"
            )
            cur.execute(sql, (id_curso,))
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    def listar_todas(self) -> List[Dict[str, Any]]:
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        try:
            sql = (
                "SELECT ac.id_alumno, ac.id_curso, ac.matriculado_en, "
                "       a.nombre AS alumno_nombre, c.nombre AS curso_nombre "
                f"FROM {self.TABLE} ac "
                "JOIN alumnos a ON a.id = ac.id_alumno "
                "JOIN cursos  c ON c.id = ac.id_curso "
                "ORDER BY ac.matriculado_en DESC"
            )
            cur.execute(sql)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()

    # --------- DELETE ----------
    def desmatricular(self, id_alumno: int, id_curso: int) -> bool:
        conn = get_connection()
        cur = conn.cursor()
        try:
            sql = f"DELETE FROM {self.TABLE} WHERE id_alumno=%s AND id_curso=%s"
            cur.execute(sql, (id_alumno, id_curso))
            conn.commit()
            return cur.rowcount == 1
        except Exception:
            conn.rollback()
            raise
        finally:
            cur.close()
            conn.close()
