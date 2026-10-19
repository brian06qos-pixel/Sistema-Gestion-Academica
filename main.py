"""Demostración integrada de las cinco fases del sistema académico."""
from modelos import ProgramaAcademico, Asignatura, Estudiante, Docente, Administrativo


def ejecutar_demo():
    print("=== SISTEMA DE GESTIÓN ACADÉMICA ===")
    sistemas = ProgramaAcademico("IS01", "Ingeniería de Sistemas", "Ciencias e Ingenierías", 10)
    administracion = ProgramaAcademico("AD01", "Administración de Empresas", "Ciencias Económicas", 9)
    asignaturas = [
        Asignatura("POO01", "Programación Orientada a Objetos", 3, sistemas),
        Asignatura("BD01", "Bases de Datos", 3, sistemas),
        Asignatura("GES01", "Gestión Organizacional", 2, administracion),
    ]
    print("\n--- Programas y asignaturas ---")
    for programa in (sistemas, administracion):
        print(programa.mostrar_informacion())
    for asignatura in asignaturas:
        print(asignatura.mostrar_informacion())

    # Una sola colección heterogénea: dos personas de cada especialización.
    personas = [
        Estudiante("1001", "Ana Gómez", "ana@ejemplo.edu", "E001", sistemas, 2, 4.3),
        Docente("2001", "Carlos Ruiz", "carlos@ejemplo.edu", "D001", "Ciencias e Ingenierías", "Tiempo completo", 40),
        Administrativo("3001", "Laura Díaz", "laura@ejemplo.edu", "A001", "Registro Académico", "Auxiliar", "Diurna"),
        Estudiante("1002", "Luis Pérez", "luis@ejemplo.edu", "E002", administracion, 3, 4.1),
        Docente("2002", "Marta López", "marta@ejemplo.edu", "D002", "Ciencias Económicas", "Cátedra", 16),
        Administrativo("3002", "Pedro Torres", "pedro@ejemplo.edu", "A002", "Biblioteca", "Coordinador", "Mixta"),
    ]
    print("\n--- Modificaciones válidas ---")
    personas[0].actualizar_correo("ana.nuevo@ejemplo.edu")
    sistemas.actualizar_semestres(9)
    asignaturas[0].actualizar_creditos(4)
    print("Correo actualizado:", personas[0].correo)
    print("Semestres actualizados:", sistemas.semestres)
    print("Créditos actualizados:", asignaturas[0].creditos)

    print("\n--- Tres intentos inválidos (controlados) ---")
    operaciones = [
        ("Correo vacío", lambda: personas[0].actualizar_correo("")),
        ("Semestres en cero", lambda: sistemas.actualizar_semestres(0)),
        ("Créditos negativos", lambda: asignaturas[0].actualizar_creditos(-2)),
    ]
    for descripcion, operacion in operaciones:
        try:
            operacion()
        except ValueError as error:
            print(f"{descripcion}: rechazado correctamente ({error})")

    print("\n--- Reporte polimórfico de personas ---")
    # Un solo ciclo, sin condicionales por tipo: Python resuelve cada método sobrescrito.
    for persona in personas:
        print(persona.mostrar_informacion())
        print("Actividad:", persona.realizar_actividad_principal())
        print("-" * 65)


if __name__ == "__main__":
    ejecutar_demo()
