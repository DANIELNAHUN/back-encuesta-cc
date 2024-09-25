from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Oficina(BaseModel):
    id_oficina: Optional[int] = None
    oficina_nombre: Optional[str] = None
    active: Optional[bool] = None
    class Config:
        orm_mode = True

class Pregunta(BaseModel):
    id_pregunta: Optional[int] = None
    texto_pregunta: Optional[str] = None
    active: Optional[bool] = None
    class Config:
        orm_mode = True

class Opcion(BaseModel):
    id_opcion: Optional[int] = None
    id_pregunta: Optional[int] = None
    texto_opcion: Optional[str] = None
    imagen_opcion: Optional[str] = None
    active: Optional[bool] = None
    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    id_respuesta: Optional[int] = None
    id_oficina: Optional[int] = None
    id_opcion_cliente: Optional[int] = None
    id_pregunta: Optional[int] = None
    id_opcion: Optional[int] = None
    date_init: Optional[datetime] = None
    date_end: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    class Config:
        orm_mode = True