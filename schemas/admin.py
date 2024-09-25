from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class Position(BaseModel):
    id_position: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    salary: Optional[float] = None
    active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    deleted_by: Optional[int] = None
    class Config:
        orm_mode = True 

class Employee(BaseModel):
    id_employee: Optional[int] = None
    name: Optional[str] = None
    last_name: Optional[str] = None
    admission_date: Optional[date] = None
    email: Optional[str] = None
    position_id: Optional[int] = None
    active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    deleted_by: Optional[int] = None
    class Config:
        orm_mode = True

class User(BaseModel):
    id_user: Optional[int] = None
    username: Optional[str] = None
    userpassword: Optional[str] = None
    employee_id: Optional[int] = None
    active: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    created_by: Optional[int] = None
    updated_by: Optional[int] = None
    deleted_by: Optional[int] = None
    class Config:
        orm_mode = True