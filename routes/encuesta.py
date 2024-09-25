import os
from datetime import datetime
from typing import Annotated, List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

import models.encuesta as models
import schemas.encuesta as schemas
from config.db import SessionLocal

encuesta = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CRUD OFICINAS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""

@encuesta.get("/oficinas/", tags=["Parametros - Sedes"], response_model=List[schemas.Oficina])
async def get_oficinas(db: db_dependency):
    oficinas = db.query(models.Oficinas).all()
    db.commit()
    return oficinas

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CRUD PREGUNTAS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""

@encuesta.get("/preguntas/", tags=["Parametros - Preguntas"], response_model=List[schemas.Pregunta])
async def get_preguntas(db: db_dependency):
    preguntas = db.query(models.Preguntas).all()
    db.commit()
    return preguntas

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CRUD OPCIONES
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@encuesta.get("/opciones/", tags=["Parametros - Opciones"], response_model=List[schemas.Opcion])
async def get_opciones(db: db_dependency, id_pregunta):
    opciones = db.query(models.Opciones).filter(models.Opciones.id_pregunta == id_pregunta).all()
    db.commit()
    return opciones

"""
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄
CRUD RESPUESTAS
༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄༄

"""
@encuesta.get("/respuestas/", tags=["Parametros - Respuestas"], response_model=List[schemas.Respuesta])
async def get_respuestas(db: db_dependency):
    respuestas = db.query(models.Respuestas).all()
    db.commit()
    return respuestas

@encuesta.post("/respuestas/", tags=["Parametros - Respuestas"], response_model=schemas.Respuesta)
async def create_respuesta(db: db_dependency, respuesta: schemas.Respuesta):
    db_respuesta = models.Respuestas(**respuesta.dict())
    db.add(db_respuesta)
    db.commit()
    db.refresh(db_respuesta)
    return db_respuesta