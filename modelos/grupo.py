"""Grupos académicos y horario compuesto."""
from datetime import time
from .persona import Estudiante, Docente, texto_obligatorio, entero_positivo
from .academico import Asignatura
from .excepciones import EstudianteYaMatriculadoError, GrupoLlenoError, EstudianteNoMatriculadoError

class Horario:
    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.dia = texto_obligatorio(dia, "Día")
        self.salon = texto_obligatorio(salon, "Salón")
        try:
            self.hora_inicio = time.fromisoformat(hora_inicio)
            self.hora_fin = time.fromisoformat(hora_fin)
        except (TypeError, ValueError) as exc:
            raise ValueError("Las horas deben tener formato HH:MM.") from exc
        if self.hora_inicio >= self.hora_fin:
            raise ValueError("La hora de inicio debe ser anterior a la de finalización.")
    def __str__(self):
        return f"{self.dia} {self.hora_inicio:%H:%M}-{self.hora_fin:%H:%M}, salón {self.salon}"

class GrupoAcademico:
    def __init__(self, codigo, asignatura, docente, capacidad_maxima, dia, hora_inicio, hora_fin, salon):
        if not isinstance(asignatura, Asignatura): raise TypeError("Se requiere un objeto Asignatura.")
        if not isinstance(docente, Docente): raise TypeError("Se requiere un objeto Docente.")
        self.codigo = texto_obligatorio(codigo, "Código del grupo")
        self.asignatura = asignatura
        self.docente = docente
        self.capacidad_maxima = entero_positivo(capacidad_maxima, "Capacidad máxima")
        self.__estudiantes = {}
        # Composición: el horario nace dentro del grupo y pertenece a este.
        self.horario = Horario(dia, hora_inicio, hora_fin, salon)
    @property
    def estudiantes(self): return tuple(self.__estudiantes.values())
    def matricular_estudiante(self, estudiante):
        if not isinstance(estudiante, Estudiante): raise TypeError("Se requiere un objeto Estudiante.")
        codigo = estudiante.codigo_estudiantil
        if codigo in self.__estudiantes:
            raise EstudianteYaMatriculadoError(f"El estudiante {codigo} ya está matriculado en {self.codigo}.")
        if len(self.__estudiantes) >= self.capacidad_maxima:
            raise GrupoLlenoError(f"El grupo {self.codigo} alcanzó su capacidad máxima.")
        self.__estudiantes[codigo] = estudiante
        return f"Matrícula exitosa: {estudiante.nombre} en {self.codigo}."
    def retirar_estudiante(self, codigo_estudiantil):
        codigo = texto_obligatorio(codigo_estudiantil, "Código estudiantil")
        if codigo not in self.__estudiantes:
            raise EstudianteNoMatriculadoError(f"El estudiante {codigo} no está matriculado en {self.codigo}.")
        estudiante = self.__estudiantes.pop(codigo)
        return f"Retiro exitoso: {estudiante.nombre} de {self.codigo}."
    def mostrar_estudiantes(self):
        if not self.__estudiantes: return "No hay estudiantes matriculados."
        return "\n".join(f"{e.codigo_estudiantil} - {e.nombre}" for e in self.__estudiantes.values())
    def mostrar_informacion_grupo(self):
        return (f"Grupo {self.codigo} | Asignatura: {self.asignatura.nombre} | "
                f"Docente: {self.docente.nombre} | Cupos: {len(self.__estudiantes)}/{self.capacidad_maxima} "
                f"| Horario: {self.horario}")
