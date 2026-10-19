# Sistema de Gestión Académica — POO en Python

**Institución:** Universidad de Manizales — Facultad de Ciencias e Ingenierías  
**Actividad:** Construcción de un Sistema de Gestión Académica utilizando Programación Orientada a Objetos  
**Integrante:** Brian David Bedoya Ramírez (trabajo individual; verificar nombre antes de entregar).

## Descripción

Primera versión de un sistema universitario que representa programas académicos, asignaturas, estudiantes, docentes y administrativos. Es **un único proyecto**, desarrollado de forma integrada, para evidenciar las cinco fases de la actividad.

## Estructura

```text
Sistema-Gestion-Academica/
├── main.py                 # Demostración ejecutable del sistema
├── modelos/
│   ├── __init__.py         # Exportación de las clases
│   ├── persona.py          # Persona, Estudiante, Docente, Administrativo
│   └── academico.py        # ProgramaAcademico, Asignatura
├── tests/
│   └── test_sistema.py     # Pruebas automatizadas
├── .gitignore
└── README.md
```

## Requisitos y ejecución

Python 3.9 o superior. No requiere instalar bibliotecas externas.

Desde la carpeta raíz del proyecto:

```bash
python main.py
```

Para ejecutar las pruebas:

```bash
python -m unittest discover -s tests -v
```

En algunos equipos se utiliza `python3` en lugar de `python`.

## Evidencia de las cinco fases

1. **Clases, objetos y constructores:** `ProgramaAcademico`, `Asignatura` y `Persona`, con inicialización en `__init__`. El programa principal crea dos programas, tres asignaturas y seis personas.
2. **Encapsulamiento:** atributos privados con `__`, propiedades de consulta y métodos de actualización. Se rechazan correos vacíos, semestres no positivos y créditos no positivos con `ValueError`. Se demuestran cambios válidos e intentos inválidos.
3. **Herencia:** `Estudiante`, `Docente` y `Administrativo` heredan de `Persona` y usan `super().__init__()` para no duplicar datos comunes.
4. **Sobreescritura:** las tres subclases implementan su propio `mostrar_informacion()` y `realizar_actividad_principal()`.
5. **Polimorfismo:** en `main.py` existe una colección heterogénea con dos instancias de cada subclase, recorrida con un único `for`, sin condicionales por tipo.

## Pruebas

El archivo `tests/test_sistema.py` comprueba constructores, consultas, actualizaciones válidas, rechazo de valores inválidos, herencia y polimorfismo. Además, `main.py` imprime el resultado de las operaciones y un reporte de las seis personas.

## Publicación y entrega en GitHub

1. Crear un repositorio en GitHub llamado `Sistema-Gestion-Academica`.
2. Subir el contenido de esta carpeta conservando la estructura.
3. Crear al menos un **commit real** correspondiente al desarrollo, con un mensaje descriptivo (por ejemplo: `Implementar modelos y pruebas del sistema académico`). No se deben fabricar commits de otras personas.
4. Comprobar que el proyecto se ejecuta y que el README se visualiza correctamente en GitHub.
5. Crear una etiqueta para esta entrega, por ejemplo `v1.0-actividad-1`, y no modificar posteriormente los archivos asociados con esa versión.
6. Entregar a la universidad el enlace real del repositorio.

Si se utiliza Git localmente, tras configurar la cuenta y crear el repositorio remoto:

```bash
git init
git add .
git commit -m "Implementar sistema académico POO y pruebas"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/Sistema-Gestion-Academica.git
git push -u origin main
git tag v1.0-actividad-1
git push origin v1.0-actividad-1
```

Reemplazar `TU_USUARIO` por el nombre real de usuario de GitHub.

## Declaración de uso de inteligencia artificial

Se utilizó **ChatGPT (OpenAI)** como apoyo para generar la estructura inicial del proyecto, implementar código Python, redactar documentación y elaborar pruebas automatizadas. El estudiante debe revisar, comprender, probar y ser capaz de explicar el código y las decisiones de diseño antes de su entrega. Esta declaración se incluye conforme a las instrucciones de la actividad.

## Observación

Los nombres, correos y códigos utilizados en la demostración son datos ficticios. El proyecto no usa base de datos ni interfaz gráfica, ya que no son requisitos de esta primera versión.
