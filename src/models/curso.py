from typing import Optional
from datetime import date, datetime

class Curso:
    def __init__(
        self,
        id: Optional[int] = None,
        nombre: str = "",
        precio: float = 0.0,
        fecha_inicio: Optional[date] = None,
        fecha_fin: Optional[date] = None,
        creado_en: Optional[datetime] = None,
        actualizado_en: Optional[datetime] = None,
    ):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.creado_en = creado_en
        self.actualizado_en = actualizado_en

    def info(self) -> str:
        fi = self.fecha_inicio.isoformat() if self.fecha_inicio else "-"
        ff = self.fecha_fin.isoformat() if self.fecha_fin else "-"
        ce = self.creado_en.strftime("%Y-%m-%d %H:%M") if self.creado_en else "-"
        ae = self.actualizado_en.strftime("%Y-%m-%d %H:%M") if self.actualizado_en else "-"
        return (
            f"id: {self.id}\n"
            f"nombre: {self.nombre}\n"
            f"precio: {self.precio:.2f}\n"
            f"fecha_inicio: {fi}\n"
            f"fecha_fin: {ff}\n"
            f"creado_en: {ce}\n"
            f"actualizado_en: {ae}\n"
        )