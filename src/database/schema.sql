-- =========================================
-- ESQUEMA: Escuela (MySQL 8+)
-- Tablas: alumnos, cursos, alumno_curso
-- =========================================

CREATE DATABASE IF NOT EXISTS escuela
  DEFAULT CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;
USE escuela;

-- alumnos
CREATE TABLE IF NOT EXISTS alumnos (
  id              INT UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre          VARCHAR(50)  NOT NULL,
  edad            TINYINT UNSIGNED NOT NULL,
  dni             CHAR(9)      NOT NULL,
  telefono        VARCHAR(20)  NULL,
  direccion       VARCHAR(100) NULL,
  creado_en       TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  actualizado_en  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY uk_alumnos_dni (dni),
  INDEX idx_alumnos_nombre (nombre),
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
CREATE TABLE IF NOT EXISTS alumno_curso (
  id_alumno       INT UNSIGNED NOT NULL,
  id_curso        INT UNSIGNED NOT NULL,
  matriculado_en  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_alumno, id_curso),
  CONSTRAINT fk_ac_alumno  FOREIGN KEY (id_alumno) REFERENCES alumnos(id)
    ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT fk_ac_curso   FOREIGN KEY (id_curso)  REFERENCES cursos(id)
    ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB;

/* -- OPCIONAL: SEED
INSERT INTO alumnos (nombre, edad, dni) VALUES
  ('Ana Pérez', 19, 'X1234567A'),
  ('Bea López', 21, 'Y7654321B');

INSERT INTO cursos (nombre, precio, fecha_inicio) VALUES
  ('Python Básico', 120.00, '2025-10-01'),
  ('SQL Express',   90.00,  '2025-10-15');

*/
