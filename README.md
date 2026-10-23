# Sistema de Gestión Académica — POO en Python

**Institución:** Universidad de Manizales  
**Actividad:** Construcción de un Sistema de Gestión Académica utilizando Programación Orientada a Objetos  
**Integrante:** Brian David Bedoya Ramírez (trabajo individual)

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

# Declaración de uso de inteligencia artificial

Se utilizó **ChatGPT (OpenAI)** como recurso para poder crear la estructura con la que se inicio el proyecto, incluir código Python de manera que no se ejecutara mal.
## Observación

Los nombres, correos y códigos utilizados en la demostración son datos ficticios. El proyecto no usa base de datos ni interfaz gráfica, ya que no son requisitos de esta primera versión.
