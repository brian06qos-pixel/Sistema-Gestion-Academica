"""Excepciones de dominio para la oferta académica."""
class EstudianteYaMatriculadoError(Exception): pass
class GrupoLlenoError(Exception): pass
class EstudianteNoMatriculadoError(Exception): pass
class AsignaturaNoEncontradaError(Exception): pass
class ProgramaNoEncontradoError(Exception): pass
