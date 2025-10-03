## Vista rápida (roles)  

- Rossana (DB & conexión, Curso)  
- Olga (Alumno)
- Noémie (Main / CLI)  
  
## Orden sugerido (para no pisarse)

- Rossana: conexión y schema ✅, Modelo + repositorio Curso, CRUD básicos con la BD lista
- Olga: Modelo + repositorio Alumno, CRUD básicos con la BD lista
- Noémie: menú con listar/crear usando repos, main.py (CLI / menús)
- Todos: actualizar/borrar + matrículas + pulir validaciones

# 🧭 Flujo diario (para todos)

- Activar el entorno (.venv)
- Tener MySQL encendido y el .env bien rellenado.
- Pull de main
- Trabajar en tu rama feature/
- pip install -r requirements.txt (por si hay cambios)
- python src/main.py para probar
- Commit + Push y abrir Pull Request

# Rossana – Base de datos y conexión

## Objetivo: tener el esquema listo, conexión estable y datos de prueba.

## Lote 1 · Imprescindible

- .env + conexión
- Hecho cuando: get_connection() conecta y cierra sin error.
- Ejecutar schema.sql (estudiantes, asignaturas, estudiante_asignatura, claves únicas y FKs)
- Hecho cuando: SHOW TABLES devuelve 3 tablas; FKs existen.
- Seed mínimo (2 alumnos, 2 cursos, 1 matrícula)
- Hecho cuando: SELECT COUNT(*) da >0 en cada tabla.
- Lote 2 · Robustez
- Índices & unicidad (dni único, nombre de asignatura único)
- Hecho cuando: insertar duplicados falla con error controlado.
- Manejo de errores en db.py (mensaje claro si no conecta)
- Hecho cuando: credenciales malas muestran error legible.
- Lote 3 · Plus
- Script backup/restore (simple mysqldump) en scripts/ con README corto.

# Olga – Modelo y Repositorio de Alumno

## Objetivo: CRUD completo + validaciones básicas.

- Lote 1 · Imprescindible
- Modelo Alumno (ya creado) revisar tipos y __repr__.
- Repo: create, get_by_id, list_all
- Hecho cuando: crear/listar funciona con datos reales.
- Validar entrada básica: nombre no vacío, edad ≥ 3, dni largo 9.
- Hecho cuando: entradas inválidas no se insertan.
- Lote 2 · Actualizar/Eliminar
- update_nombre y delete
- Hecho cuando: actualizar y eliminar devuelven True/False según filas afectadas.
- Buscar por nombre (parcial) find_by_name(substr)
- Hecho cuando: devuelve lista filtrada y ordenada.
- Lote 3 · Plus
- Normalización de nombre (title(), quitar espacios dobles).
- Prueba manual: pequeño script que cree 2 alumnos y los imprima.
- Criterio de Done (Olga): repo sin print internos (devuelve datos/booleans), errores capturados y docstrings breves.

# Rossana – Modelo y Repositorio de Curso

## Objetivo: CRUD de cursos + fechas.

- Lote 1 · Imprescindible
- Modelo Curso (ya creado) comprobar date opcional.
- Repo: create, get_by_id, list_all
- Hecho cuando: se puede crear y listar cursos.
- Validaciones: nombre no vacío; si hay fechas → inicio ≤ fin.
- Lote 2 · Actualizar/Eliminar
- update_nombre y delete
- Hecho cuando: cambian/borra según id.
- Lote 3 · Plus
- Parsers: función para convertir "dd/mm/aaaa" → date.
- Búsqueda find_by_name(substr).
- Criterio de Done (Efra): no rompe si fechas son None; mensajes de error legibles al validar.

# Noémie – Main / CLI  

## Objetivo: un menú simple para probar sin tocar SQL 

- Lote 1 · Menú mínimo
- Menú principal (texto)
- Opciones: 1) Alumnos 2) Cursos 3) Matrículas 0) Salir.
- Submenús
- Alumnos: crear, listar, buscar por nombre, actualizar nombre, borrar.
- Cursos: crear, listar, actualizar nombre, borrar.
- Lote 2 · Matrículas
- Inscribir alumno en curso (MatriculaRepository.enroll)
- Hecho cuando: muestra confirmación y aparece en “listar cursos de un alumno”.
- Listar
- “Cursos de un alumno” y “Alumnos de un curso”.
- Lote 3 · UX & Validación
- Entrada segura (int() con try/except, fechas opcionales)
- Impresión bonita (tablas sencillas, encabezados).
- Criterio de Done (Noémie): ningún input revienta la app; al cancelar (Enter vacío) vuelve al menú sin crash.

# Tareas transversales (todas)  

- Convenciones: snake_case, funciones cortas, docstrings 1–2 líneas.
- Commits pequeños: “feat: create() de alumno”, “fix: validar dni”.

# Ramas por feature  

- feature/alumno, feature/curso, feature/cli, feature/db-connection.
- Pull Request: descripción breve + cómo probarlo.
