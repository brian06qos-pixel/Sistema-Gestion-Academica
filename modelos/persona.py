"""Personas vinculadas a la universidad y sus especializaciones."""


def texto_obligatorio(valor, campo):
    if not isinstance(valor, str) or not valor.strip():
        raise ValueError(f"{campo} no puede estar vacío.")
    return valor.strip()


def entero_positivo(valor, campo):
    if type(valor) is not int or valor <= 0:
        raise ValueError(f"{campo} debe ser un entero mayor que cero.")
    return valor


class Persona:
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = texto_obligatorio(identificacion, "Identificación")
        self.__nombre = texto_obligatorio(nombre, "Nombre")
        self.__correo = ""
        self.actualizar_correo(correo)

    @property
    def identificacion(self):
        return self.__identificacion

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def actualizar_correo(self, nuevo_correo):
        self.__correo = texto_obligatorio(nuevo_correo, "Correo electrónico")

    def mostrar_informacion(self):
        return f"Identificación: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"

    def realizar_actividad_principal(self):
        return "Participa en la comunidad universitaria."


class Estudiante(Persona):
    def __init__(self, identificacion, nombre, correo, codigo_estudiantil, programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        from .academico import ProgramaAcademico
        if not isinstance(programa, ProgramaAcademico):
            raise ValueError("El programa debe ser un ProgramaAcademico.")
        self.__codigo_estudiantil = texto_obligatorio(codigo_estudiantil, "Código estudiantil")
        self.__programa = programa
        self.__semestre = entero_positivo(semestre, "Semestre")
        self.__promedio = 0.0
        self.actualizar_promedio(promedio)

    @property
    def promedio(self):
        return self.__promedio

    def actualizar_promedio(self, valor):
        if isinstance(valor, bool) or not isinstance(valor, (int, float)) or not 0 <= valor <= 5:
            raise ValueError("El promedio debe estar entre 0 y 5.")
        self.__promedio = float(valor)

    def mostrar_informacion(self):
        return (f"[Estudiante] {super().mostrar_informacion()} | Código: {self.__codigo_estudiantil} "
                f"| Programa: {self.__programa.nombre} | Semestre: {self.__semestre} | Promedio: {self.__promedio:.2f}")

    def realizar_actividad_principal(self):
        return f"Cursa {self.__programa.nombre} en el semestre {self.__semestre}."


class Docente(Persona):
    def __init__(self, identificacion, nombre, correo, numero_empleado, facultad, tipo_contratacion, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = texto_obligatorio(numero_empleado, "Número de empleado")
        self.__facultad = texto_obligatorio(facultad, "Facultad")
        self.__tipo_contratacion = texto_obligatorio(tipo_contratacion, "Tipo de contratación")
        self.__horas_semanales = entero_positivo(horas_semanales, "Horas semanales")

    def mostrar_informacion(self):
        return (f"[Docente] {super().mostrar_informacion()} | Empleado: {self.__numero_empleado} "
                f"| Facultad: {self.__facultad} | Contratación: {self.__tipo_contratacion} "
                f"| Horas semanales: {self.__horas_semanales}")

    def realizar_actividad_principal(self):
        return f"Orienta clases en la facultad de {self.__facultad}."


class Administrativo(Persona):
    def __init__(self, identificacion, nombre, correo, numero_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__numero_empleado = texto_obligatorio(numero_empleado, "Número de empleado")
        self.__dependencia = texto_obligatorio(dependencia, "Dependencia")
        self.__cargo = texto_obligatorio(cargo, "Cargo")
        self.__jornada = texto_obligatorio(jornada, "Jornada")

    def mostrar_informacion(self):
        return (f"[Administrativo] {super().mostrar_informacion()} | Empleado: {self.__numero_empleado} "
                f"| Dependencia: {self.__dependencia} | Cargo: {self.__cargo} | Jornada: {self.__jornada}")

    def realizar_actividad_principal(self):
        return f"Desempeña el cargo de {self.__cargo} en {self.__dependencia}."
