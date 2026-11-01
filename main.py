"""Demostración de los once casos mínimos de la Actividad Colaborativa 2."""
from modelos import (Persona, ProgramaAcademico, Asignatura, Estudiante, Docente,
    Administrativo, GrupoAcademico, CatalogoAcademico, EstudianteYaMatriculadoError,
    GrupoLlenoError, EstudianteNoMatriculadoError, AsignaturaNoEncontradaError,
    ProgramaNoEncontradoError)

def intentar(etiqueta, operacion):
    print(f"\n{etiqueta}")
    try:
        resultado = operacion()
        if resultado is not None: print(resultado)
    except (TypeError, EstudianteYaMatriculadoError, GrupoLlenoError,
            EstudianteNoMatriculadoError, AsignaturaNoEncontradaError,
            ProgramaNoEncontradoError) as error:
        print(f"Excepción controlada: {error}")

def main():
    print("SISTEMA DE GESTIÓN ACADÉMICA - ACTIVIDAD 2")
    intentar("1. Instanciación de Persona prohibida", lambda: Persona("0", "Persona", "p@u.edu"))
    programa = ProgramaAcademico("IS", "Ingeniería de Sistemas", "Ingenierías", 10)
    programa2 = ProgramaAcademico("AD", "Administración", "Ciencias Económicas", 9)
    asignatura = Asignatura("POO", "Programación Orientada a Objetos", 3, programa)
    asignatura2 = Asignatura("BD", "Bases de Datos", 3, programa)
    docente = Docente("10", "Laura Torres", "laura@u.edu", "D10", "Ingenierías", "Tiempo completo", 40)
    e1 = Estudiante("1", "Ana Ruiz", "ana@u.edu", "E01", programa, 2, 4.2)
    e2 = Estudiante("2", "Luis Díaz", "luis@u.edu", "E02", programa, 2, 4.0)
    e3 = Estudiante("3", "Sara Pérez", "sara@u.edu", "E03", programa, 2, 4.4)
    administrativo = Administrativo("11", "Marta Gil", "marta@u.edu", "A11", "Registro", "Auxiliar", "Diurna")
    catalogo = CatalogoAcademico()
    for p in (programa, programa2): catalogo.agregar_programa(p)
    for a in (asignatura, asignatura2): catalogo.agregar_asignatura(a)
    grupo1 = GrupoAcademico("G01", asignatura, docente, 2, "Lunes", "18:00", "20:00", "A101")
    grupo2 = GrupoAcademico("G02", asignatura2, docente, 3, "Miércoles", "18:00", "20:00", "B202")
    print("\n2 y 3. Objetos creados y dos grupos con horarios")
    print(grupo1.mostrar_informacion_grupo()); print(grupo2.mostrar_informacion_grupo())
    intentar("4. Matrícula correcta", lambda: grupo1.matricular_estudiante(e1))
    intentar("5. Matrícula duplicada", lambda: grupo1.matricular_estudiante(e1))
    intentar("4. Segunda matrícula correcta", lambda: grupo1.matricular_estudiante(e2))
    intentar("6. Grupo lleno", lambda: grupo1.matricular_estudiante(e3))
    intentar("7. Retiro correcto", lambda: grupo1.retirar_estudiante("E02"))
    intentar("8. Retiro inexistente", lambda: grupo1.retirar_estudiante("E99"))
    intentar("9. Asignatura inexistente", lambda: catalogo.buscar_asignatura("XYZ"))
    intentar("10. Programa inexistente", lambda: catalogo.buscar_programa("XYZ"))
    print("\nEstudiantes del grupo G01:\n" + grupo1.mostrar_estudiantes())
    print("\nPolimorfismo conservado de AC1:")
    for persona in (e1, docente, administrativo): print(persona.realizar_actividad_principal())
    print("\n11. El programa continúa y finaliza correctamente.")
if __name__ == "__main__": main()
