# Driving School System

## Description
The goal is to design an ADT to manage students under different instructors in a driving school. Both students and instructors are identified by their names, which are strings. The following operations should be supported:

### Operations
- **init**: Initially, no instructor has assigned students.
- **alta(A, P)**: Registers a student or changes their instructor. If the student is new, they are assigned a score of zero. If transferring, the student is removed from their previous instructor while retaining their score and is assigned to the new instructor.
- **es_alumno(A, P)**: Checks if student `A` is currently registered under instructor `P`.
- **puntuacion(A)**: Returns the score of student `A`. If `A` is not enrolled, a domain error is thrown with the message: `El alumno A no esta matriculado.`
- **actualizar(A, N)**: Increases student `A`'s score by `N`. If `A` is not enrolled, a domain error is thrown with the message: `El alumno A no esta matriculado.`
- **examen(P, N)**: Returns a list of students under instructor `P` who qualify for the exam (students with a score of `N` or higher), sorted alphabetically.
- **aprobar(A)**: Removes student `A` from the driving school upon passing the exam. All information about `A` is deleted. If `A` is not enrolled, a domain error is thrown with the message: `El alumno A no esta matriculado.`

## Implementation Requirements
- Select an appropriate data structure to store the information.
- Each function must specify its computational cost.
- ADT methods must not produce any output directly.
- Input and output handling must be done through external functions.

## Input Format
Each test case consists of multiple lines representing operations on an initially empty driving school. The format is:
```
[operation] [arguments]
```
Each test case ends with a line containing `FIN`. Student and instructor names do not contain spaces.

## Output Format
Each test case generates output based on the requested operations:
- **es_alumno**: Outputs `A es alumno de P` or `A no es alumno de P`.
- **puntuacion**: Outputs `Puntuacion de A: X`, where `X` is the score of `A`.
- **examen**: Outputs `Alumnos de P a examen:`, followed by a line for each eligible student, sorted alphabetically.

Each test case ends with a line containing `---`.
If an operation results in an error, the output is `ERROR`, and no further output is generated for that operation.

## Extra

For each student and professor, it must be possible to store the name, surname and a telephone number.

## Example
### Input
```
alta Luis Paco
alta Marta Paco
es_alumno Luis Paco
es_alumno Marta Ramon
examen Paco 0
actualizar Marta 10
examen Paco 10
examen Juan 10
alta Marta Juan
puntuacion Marta
actualizar Marta 10
examen Juan 20
actualizar Miguel 5
aprobar Marta
examen Juan 20
FIN
puntuacion Alejandro
alta Alejandro Isabel
actualizar Alejandro 20
puntuacion Alejandro
aprobar Alejandro
puntuacion Alejandro
FIN
```

### Output
```
Luis es alumno de Paco
Marta no es alumno de Ramon
Alumnos de Paco a examen:
Luis
Marta
Alumnos de Paco a examen:
Marta
Alumnos de Juan a examen:
Puntuacion de Marta: 10
Alumnos de Juan a examen:
Marta
ERROR
Alumnos de Juan a examen:
---
ERROR
Puntuacion de Alejandro: 20
ERROR
---
```

