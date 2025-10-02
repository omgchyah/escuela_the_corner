-- =========================================
-- ESQUEMA: Escuela (MySQL 8+)
-- Tablas: estudiantes, cursos, estudiante_curso
-- =========================================

CREATE DATABASE IF NOT EXISTS escuela
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_0900_ai_ci;
USE escuela;

-- Estudiantes
CREATE TABLE IF NOT EXISTS estudiantes (
  id              INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre          VARCHAR(50)  NOT NULL,
  edad            TINYINT UNSIGNED NOT NULL,
  dni             CHAR(9)      NOT NULL,
  telefono        VARCHAR(20)  NULL,
  direccion       VARCHAR(100) NULL,
  creado_en       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_estudiantes_dni (dni),
  INDEX idx_estudiantes_nombre (nombre),
  CHECK (edad BETWEEN 3 AND 120)
) ENGINE=InnoDB;

-- Cursos (antes 'asignaturas'), con precio
CREATE TABLE IF NOT EXISTS cursos (
  id              INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre          VARCHAR(50)  NOT NULL,
  precio          DECIMAL(10,2) NOT NULL,               -- € precio del curso
  fecha_inicio    DATE         NULL,
  fecha_fin       DATE         NULL,
  creado_en       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_cursos_nombre (nombre),
  CHECK (precio >= 0),
  CHECK (fecha_inicio IS NULL OR fecha_fin IS NULL OR fecha_inicio <= fecha_fin)
) ENGINE=InnoDB;

-- Relación muchos-a-muchos (matrículas)
CREATE TABLE IF NOT EXISTS estudiante_curso (
  id_estudiante   INT UNSIGNED NOT NULL,
  id_curso        INT UNSIGNED NOT NULL,
  matriculado_en  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_estudiante, id_curso),
  CONSTRAINT fk_ec_estudiante
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ec_curso
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

/* -- OPCIONAL: SEED
INSERT INTO estudiantes (nombre, edad, dni) VALUES
  ('Ana Pérez', 18, 'X1234567A'),
  ('Luis Gómez', 20, 'Y7654321B');

INSERT INTO cursos (nombre, precio, fecha_inicio, fecha_fin) VALUES
  ('Matemáticas', 199.99, '2025-10-01', '2026-03-01'),
  ('Historia',     99.00, '2025-10-01', '2026-02-15');

INSERT INTO estudiante_curso (id_estudiante, id_curso) VALUES (1,1),(2,2);
*/
