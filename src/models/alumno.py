# Método constructor __init__ y guarda datos (Plantilla para objetos)

from typing import Optional
from datetime import datetime

class Alumno:
    
    def __init__(
        self,
        id: Optional[int] = None,
        nombre: str = "",
        edad: int = 0,
        dni: str = "",
        telefono: Optional [str] = None,
        direccion: Optional [str] = None,
        creado_en: Optional[datetime] = None,
        actualizado_en: Optional[datetime] = None,
    ):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.direccion = direccion
        self.creado_en = creado_en
        self.actualizado_en = actualizado_en
        
# Método info que devuelve una cadena con la información del alumno

    def info(self):
        return (
            f"id : {self.id}\n"
            f"nombre : {self.nombre}\n"
            f"edad : {self.edad}\n"
            f"dni : {self.dni}\n"
            f"teléfono : {self.telefono}\n"
            f"dirección : {self.direccion}\n"
            f"creado en : {self.creado_en}\n"
            f"actualizado en : {self.actualizado_en}\n"
            )

# Dos instancias (dos alumnos)
    
alumno1 = Alumno(22, "Pepe", 24, "45682179K", 686924775, "carrer aribau, 4, 1º 2º")

alumno2 = Alumno(55, "Rossana", 22, "12845914L", 688154933, "carrer arús, 12, 3º 1º")

alumno3 = Alumno(None, "Raquel", 33, "41854617N")

# Ejecutga el método info sobre el objeto y devuelve la cadena con sus datos

info_alumno1 = alumno1.info()

# Imprime en consola la información

print(f"{alumno1.info()}\n{alumno2.info()}\n{alumno3.info()}")