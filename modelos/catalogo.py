"""Búsquedas de programas y asignaturas por código."""
from .academico import ProgramaAcademico, Asignatura
from .excepciones import AsignaturaNoEncontradaError, ProgramaNoEncontradoError
class CatalogoAcademico:
    def __init__(self):
        self.programas = {}
        self.asignaturas = {}
    def agregar_programa(self, programa):
        if not isinstance(programa, ProgramaAcademico): raise TypeError("Se requiere un ProgramaAcademico.")
        self.programas[programa.codigo] = programa
    def agregar_asignatura(self, asignatura):
        if not isinstance(asignatura, Asignatura): raise TypeError("Se requiere una Asignatura.")
        self.asignaturas[asignatura.codigo] = asignatura
    def buscar_programa(self, codigo):
        if codigo not in self.programas: raise ProgramaNoEncontradoError(f"No existe el programa {codigo}.")
        return self.programas[codigo]
    def buscar_asignatura(self, codigo):
        if codigo not in self.asignaturas: raise AsignaturaNoEncontradaError(f"No existe la asignatura {codigo}.")
        return self.asignaturas[codigo]
