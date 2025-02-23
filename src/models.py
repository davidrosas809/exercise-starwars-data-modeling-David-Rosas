import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    id: Mapped[int] = mapped_column(primary_key=True)



    #Relaciones de las bases de dtos ---------->

    usuario_id: Mapped[str] = mapped_column(ForeignKey('usuario.id'), nullable=True)
    usuario: Mapped["Usuario"] = relationship()
    
    planetas_id: Mapped[str] = mapped_column(ForeignKey('planetas.id'), nullable=True)
    favoritos: Mapped["Planetas"] = relationship()
    
    personajes_id: Mapped[str] = mapped_column(ForeignKey('personajes.id'), nullable=True)
    personajes: Mapped["Personajes"] = relationship()

class Planetas(Base):
    __tablename__ = 'planetas'
    id: Mapped[int] = mapped_column(primary_key=True)
    Name: Mapped[str] = mapped_column(nullable=True)
    gravity: Mapped[str] = mapped_column(nullable=True)
    diameter: Mapped[str] = mapped_column(nullable=True)
    terrain: Mapped[str] = mapped_column(nullable=True)
    climate: Mapped[str] = mapped_column(nullable=True)  

class Personajes(Base):
    __tablename__= 'personajes'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=True)
    height: Mapped[str] = mapped_column(nullable=True)
    gender: Mapped[str] = mapped_column(nullable=True)
    birth_year: Mapped[str] = mapped_column(nullable=True)
    eye_color: Mapped[str] = mapped_column(nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
