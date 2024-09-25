CREATE DATABASE encuestas_cc;
USE encuestas_cc;


CREATE TABLE oficinas(
    id_oficina INT NOT NULL AUTO_INCREMENT,
    oficina_nombre VARCHAR(250) NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    PRIMARY KEY (id_oficina)
);

CREATE TABLE preguntas(
    id_pregunta INT NOT NULL AUTO_INCREMENT,
    texto_pregunta VARCHAR(250) NOT NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    PRIMARY KEY (id_pregunta)
);

CREATE TABLE opciones(
    id_opcion INT NOT NULL AUTO_INCREMENT,
    id_pregunta INT NOT NULL,
    texto_opcion VARCHAR(250) NOT NULL,
    imagen_opcion VARCHAR(250) NULL,
    active BOOLEAN NOT NULL DEFAULT 1,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    PRIMARY KEY (id_opcion)
);
ALTER TABLE opciones ADD FOREIGN KEY (id_pregunta) REFERENCES preguntas(id_pregunta);

CREATE TABLE respuestas(
    id_respuesta INT NOT NULL AUTO_INCREMENT,
    id_oficina INT NOT NULL,
    id_pregunta INT NOT NULL,
    id_opcion INT NOT NULL,
    date_init DATETIME NOT NULL,
    date_end DATETIME NOT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at DATETIME NULL,
    PRIMARY KEY (id_respuesta)
);
ALTER TABLE respuestas ADD FOREIGN KEY (id_oficina) REFERENCES oficinas(id_oficina);
ALTER TABLE respuestas ADD FOREIGN KEY (id_pregunta) REFERENCES preguntas(id_pregunta);
ALTER TABLE respuestas ADD FOREIGN KEY (id_opcion) REFERENCES opciones(id_opcion);

CREATE VIEW v_respuestas AS
SELECT
    r.id_respuesta,
    o.oficina_nombre,
    p.texto_pregunta,
    o.texto_opcion,
    r.date_init,
    r.date_end
FROM respuestas r
INNER JOIN oficinas o ON r.id_oficina = o.id_oficina
INNER JOIN preguntas p ON r.id_pregunta = p.id_pregunta
INNER JOIN opciones op ON r.id_opcion = op.id_opcion;