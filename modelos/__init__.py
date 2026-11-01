"""Modelos del sistema académico."""
from .academico import ProgramaAcademico, Asignatura
from .persona import Persona, Estudiante, Docente, Administrativo
from .grupo import GrupoAcademico, Horario
from .catalogo import CatalogoAcademico
from .excepciones import (EstudianteYaMatriculadoError, GrupoLlenoError,
    EstudianteNoMatriculadoError, AsignaturaNoEncontradaError, ProgramaNoEncontradoError)
