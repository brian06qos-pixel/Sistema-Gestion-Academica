"""Pruebas automatizadas sin dependencias externas (unittest)."""
import unittest
from modelos import Persona, ProgramaAcademico, Asignatura, Estudiante, Docente, Administrativo


class PruebasSistema(unittest.TestCase):
    def setUp(self):
        self.programa = ProgramaAcademico("IS", "Sistemas", "Ingeniería", 10)
        self.asignatura = Asignatura("POO", "POO", 3, self.programa)
        self.estudiante = Estudiante("1", "Ana", "a@u.edu", "E1", self.programa, 2, 4.2)

    def test_constructores_y_consultas(self):
        self.assertEqual(self.programa.semestres, 10)
        self.assertEqual(self.asignatura.programa, self.programa)
        self.assertIn("Ana", self.estudiante.mostrar_informacion())

    def test_actualizaciones_validas(self):
        self.estudiante.actualizar_correo("nuevo@u.edu")
        self.programa.actualizar_semestres(8)
        self.asignatura.actualizar_creditos(4)
        self.estudiante.actualizar_promedio(4.8)
        self.assertEqual((self.estudiante.correo, self.programa.semestres, self.asignatura.creditos, self.estudiante.promedio),
                         ("nuevo@u.edu", 8, 4, 4.8))

    def test_correo_vacio(self):
        with self.assertRaises(ValueError):
            self.estudiante.actualizar_correo("  ")
        self.assertEqual(self.estudiante.correo, "a@u.edu")

    def test_semestres_invalidos(self):
        with self.assertRaises(ValueError):
            self.programa.actualizar_semestres(0)
        self.assertEqual(self.programa.semestres, 10)

    def test_creditos_invalidos(self):
        with self.assertRaises(ValueError):
            self.asignatura.actualizar_creditos(-1)
        self.assertEqual(self.asignatura.creditos, 3)

    def test_promedio_invalido(self):
        with self.assertRaises(ValueError):
            self.estudiante.actualizar_promedio(5.5)

    def test_herencia_y_polimorfismo(self):
        personas = [
            self.estudiante,
            Docente("2", "Luis", "l@u.edu", "D1", "Ingeniería", "Cátedra", 12),
            Administrativo("3", "Eva", "e@u.edu", "A1", "Biblioteca", "Auxiliar", "Diurna"),
        ]
        self.assertTrue(all(isinstance(p, Persona) for p in personas))
        actividades = [p.realizar_actividad_principal() for p in personas]
        self.assertEqual(len(set(actividades)), 3)
        self.assertTrue(all(p.mostrar_informacion() for p in personas))


if __name__ == "__main__":
    unittest.main()
