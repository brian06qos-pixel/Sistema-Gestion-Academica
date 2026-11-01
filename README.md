# Sistema de Gestión Académica — Actividad Colaborativa N.º 2

**Universidad de Manizales — Programación Orientada a Objetos**  
**Integrante:** Brian David Bedoya Ramírez (trabajo individual)  
**Repositorio original:** https://github.com/brian06qos-pixel/Sistema-Gestion-Academica

## Descripción
Evolución del sistema de la Actividad 1. Se conservan las clases de personas, programas y asignaturas y se agregan abstracción, composición, grupos académicos, matrículas, búsquedas y excepciones personalizadas.

## Requisitos y ejecución
Python 3.9 o superior; no requiere bibliotecas externas.

```bash
python main.py
python -m unittest discover -s tests -v
```

## Organización
- `modelos/persona.py`: Persona abstracta, Estudiante, Docente y Administrativo.
- `modelos/academico.py`: ProgramaAcademico y Asignatura.
- `modelos/grupo.py`: GrupoAcademico y Horario.
- `modelos/catalogo.py`: búsquedas de asignaturas y programas.
- `modelos/excepciones.py`: cinco excepciones de negocio.
- `tests/test_ac2.py`: pruebas automatizadas de la evolución.
- `main.py`: demostración de los 11 casos mínimos.
- `Documento_Decisiones_Diseno_AC2.docx`: explicación técnica de las decisiones.

## Composición frente a herencia
Un grupo **tiene un** horario, pero no **es un** horario. Por eso `GrupoAcademico` crea y conserva un objeto `Horario` en su constructor; es composición, no herencia. Por contraste, Estudiante **es una** Persona, por lo que sí corresponde la herencia.

## Excepciones personalizadas
`EstudianteYaMatriculadoError`, `GrupoLlenoError`, `EstudianteNoMatriculadoError`, `AsignaturaNoEncontradaError` y `ProgramaNoEncontradoError` se lanzan en las operaciones que detectan los problemas y se capturan en `main.py` para continuar la demostración.

## Continuidad con AC1
`Persona` conserva sus datos y métodos, pero ahora hereda de `ABC` y declara `realizar_actividad_principal()` con `@abstractmethod`. Sus tres subclases conservan las implementaciones especializadas. Se mantienen encapsulamiento, sobreescritura y polimorfismo.

## Versionado y entrega
**Antes de subir esta versión**, identificar el último commit de la Actividad 1 mediante una etiqueta `Entrega_AC1` si aún no existe. Subir después los archivos de esta carpeta al **mismo** repositorio, registrar al menos un commit propio de AC2 y crear el tag `Entrega_AC2` apuntando al commit final. No reescribir el historial de AC1.

## Uso de inteligencia artificial
Se utilizó ChatGPT (OpenAI) como apoyo para estructurar y redactar código, preparar pruebas, revisar la solución y elaborar documentación. El integrante debe verificar el funcionamiento, comprender y poder justificar todas las decisiones antes de entregar.
