import unittest
from modelos import *
class PruebasAC2(unittest.TestCase):
    def setUp(self):
        self.p = ProgramaAcademico("P1", "Sistemas", "Ingeniería", 10)
        self.a = Asignatura("A1", "POO", 3, self.p)
        self.d = Docente("1", "Docente", "d@u.edu", "D1", "Ingeniería", "Planta", 40)
        self.e1 = Estudiante("2", "Estudiante 1", "e1@u.edu", "E1", self.p, 2, 4)
        self.e2 = Estudiante("3", "Estudiante 2", "e2@u.edu", "E2", self.p, 2, 4)
        self.g = GrupoAcademico("G1", self.a, self.d, 1, "Lunes", "08:00", "10:00", "101")
    def test_persona_abstracta(self):
        with self.assertRaises(TypeError): Persona("0", "X", "x@u.edu")
    def test_herencia_y_polimorfismo(self):
        admin = Administrativo("4", "Admin", "a@u.edu", "A4", "Registro", "Auxiliar", "Diurna")
        for persona in (self.e1, self.d, admin):
            self.assertIsInstance(persona, Persona)
            self.assertIsInstance(persona.realizar_actividad_principal(), str)
    def test_composicion(self):
        self.assertIsInstance(self.g.horario, Horario)
        self.assertIn("Lunes", str(self.g.horario))
    def test_matricula_y_duplicado(self):
        self.g.matricular_estudiante(self.e1)
        self.assertEqual(len(self.g.estudiantes), 1)
        with self.assertRaises(EstudianteYaMatriculadoError): self.g.matricular_estudiante(self.e1)
    def test_cupo(self):
        self.g.matricular_estudiante(self.e1)
        with self.assertRaises(GrupoLlenoError): self.g.matricular_estudiante(self.e2)
    def test_retiro(self):
        self.g.matricular_estudiante(self.e1)
        self.g.retirar_estudiante("E1")
        self.assertEqual(len(self.g.estudiantes), 0)
        with self.assertRaises(EstudianteNoMatriculadoError): self.g.retirar_estudiante("E1")
    def test_busquedas(self):
        c = CatalogoAcademico(); c.agregar_programa(self.p); c.agregar_asignatura(self.a)
        self.assertIs(c.buscar_programa("P1"), self.p)
        self.assertIs(c.buscar_asignatura("A1"), self.a)
        with self.assertRaises(ProgramaNoEncontradoError): c.buscar_programa("P2")
        with self.assertRaises(AsignaturaNoEncontradaError): c.buscar_asignatura("A2")
    def test_validacion_horario(self):
        with self.assertRaises(ValueError): Horario("Lunes", "11:00", "10:00", "101")
    def test_validacion_tipos(self):
        with self.assertRaises(TypeError): GrupoAcademico("G", "POO", self.d, 1, "Lunes", "08:00", "10:00", "101")
        with self.assertRaises(TypeError): self.g.matricular_estudiante("E1")
if __name__ == "__main__": unittest.main()
