"""Programas académicos y asignaturas de la universidad."""
from .persona import texto_obligatorio, entero_positivo


class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, semestres):
        self.__codigo = texto_obligatorio(codigo, "Código")
        self.__nombre = texto_obligatorio(nombre, "Nombre")
        self.__facultad = texto_obligatorio(facultad, "Facultad")
        self.__semestres = 1
        self.actualizar_semestres(semestres)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def facultad(self):
        return self.__facultad

    @property
    def semestres(self):
        return self.__semestres

    def actualizar_semestres(self, valor):
        self.__semestres = entero_positivo(valor, "Número de semestres")

    def mostrar_informacion(self):
        return (f"Programa: {self.nombre} | Código: {self.codigo} | Facultad: {self.facultad} "
                f"| Semestres: {self.semestres}")


class Asignatura:
    def __init__(self, codigo, nombre, creditos, programa):
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("La asignatura requiere un ProgramaAcademico.")
        self.__codigo = texto_obligatorio(codigo, "Código")
        self.__nombre = texto_obligatorio(nombre, "Nombre")
        self.__programa = programa
        self.__creditos = 1
        self.actualizar_creditos(creditos)

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def creditos(self):
        return self.__creditos

    @property
    def programa(self):
        return self.__programa

    def actualizar_creditos(self, valor):
        self.__creditos = entero_positivo(valor, "Número de créditos")

    def mostrar_informacion(self):
        return (f"Asignatura: {self.nombre} | Código: {self.codigo} | Créditos: {self.creditos} "
                f"| Programa: {self.programa.nombre}")
