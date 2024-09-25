from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Text, DateTime, Date, Float

from config.db import Base

class Oficinas(Base):
    __tablename__ = "oficinas"

    id_oficina = Column(Integer, primary_key=True, index=True)
    oficina_nombre = Column(String(250))
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Preguntas(Base):
    __tablename__ = "preguntas"

    id_pregunta = Column(Integer, primary_key=True, index=True)
    texto_pregunta = Column(String(250))
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Opciones(Base):
    __tablename__ = "opciones"

    id_opcion = Column(Integer, primary_key=True, index=True)
    id_pregunta = Column(Integer, ForeignKey("preguntas.id_pregunta"))
    texto_opcion = Column(String(250))
    imagen_opcion = Column(String(250))
    active = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Respuestas(Base):
    __tablename__ = "respuestas"

    id_respuesta = Column(Integer, primary_key=True, index=True)
    id_oficina = Column(Integer, ForeignKey("oficinas.id_oficina"))
    id_opcion_cliente = Column(Integer, ForeignKey("opciones.id_opcion"))
    id_pregunta = Column(Integer, ForeignKey("preguntas.id_pregunta"))
    id_opcion = Column(Integer, ForeignKey("opciones.id_opcion"))
    date_init = Column(DateTime)
    date_end = Column(DateTime)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)

class V_Respuestas(Base):
    __tablename__ = "v_respuestas"

    id_respuesta = Column(Integer, primary_key=True, index=True)
    oficina_nombre = Column(String(250))
    texto_pregunta = Column(String(250))
    texto_opcion = Column(String(250))
    date_init = Column(DateTime)
    date_end = Column(DateTime)