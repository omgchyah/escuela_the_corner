import os
import re
from pathlib import Path
from mysql.connector import connect, Error
from dotenv import load_dotenv, find_dotenv

# Carga variables desde .env en la raíz del repo
load_dotenv(find_dotenv())

DB_NAME    = os.getenv("DB_NAME", "escuela")
DB_HOST    = os.getenv("DB_HOST", "localhost")
DB_PORT    = int(os.getenv("DB_PORT", "3306"))
DB_USER    = os.getenv("DB_USER", "root")
DB_PASS    = os.getenv("DB_PASSWORD", "")

DB_CHARSET = "utf8mb4"
DB_COLLATE = "utf8mb4_general_ci"

def _server_conn():
    """Conexión al servidor (sin seleccionar BD)."""
    try:
        return connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
        )
    except Error as e:
        raise RuntimeError(f"❌ No pude conectar al servidor MySQL: {e}")

def ensure_database():
    try:
        with _server_conn() as conn, conn.cursor() as cur:
            cur.execute(
                f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
                f"DEFAULT CHARACTER SET {DB_CHARSET} "
                f"COLLATE {DB_COLLATE};"
            )
            conn.commit()  # ← explícito
    except Error as e:
        raise RuntimeError(f"❌ No pude crear/asegurar la BD '{DB_NAME}': {e}")

def get_connection():
    """Devuelve conexión a la BD (asegurando que exista)."""
    ensure_database()
    try:
        return connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME,
        )
    except Error as e:
        raise RuntimeError(f"❌ Falló la conexión a '{DB_NAME}': {e}")

def run_schema(script_path: str | None = None):
    ensure_database()
    path = Path(script_path) if script_path else Path(__file__).with_name("schema.sql")
    content = path.read_text(encoding="utf-8")

    # Quita comentarios /* ... */ y -- en línea
    content = re.sub(r"/\*.*?\*/", "", content, flags=re.S)
    lines = []
    for raw in content.splitlines():
        line = raw.split("--", 1)[0].strip()
        if line:
            lines.append(line)

    # Acumula hasta ';' y ejecuta
    statements, stmt = [], []
    for line in lines:
        stmt.append(line)
        if line.endswith(";"):
            statements.append(" ".join(stmt))
            stmt = []

    with _server_conn() as conn, conn.cursor() as cur:
        cur.execute(f"USE `{DB_NAME}`;")
        for s in statements:
            cur.execute(s)

def test_connection() -> bool:
    """Ping rápido para verificar conectividad."""
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute("SELECT 1")
            cur.fetchone()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == "__main__":
    # Útil para ejecutar este archivo directamente:
    ensure_database()
    run_schema()       # Aplica el schema si aún no existe (es idempotente)
    print("✅ BD creada/asegurada y esquema aplicado.")