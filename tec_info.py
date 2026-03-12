"""

Universidad: Instituto Tecnológico de Costa Rica
Escuela: Ingeniería en Computadores
Curso: Introducción a la Programación
Año: 2026
Grupo: n/a
Versión de Python: 3.14.3

Estudiantes: Brenda y Ericka Villalobos
Título: Introducción a Python
Descripción: Creacion de biblioteca personalizada
Versión del programa: 1.0
Requerimientos del sistema: Python 3.8 o superior

"""
#--------------------------------------------------------------------------------------------


#Variables

uni = "Instituto Tecnologico de Costa Rica"
escuela = "Ingenieria en computadores"
curso = "Introduccion a la programacion"
año = "2026"
version = "3.14.3"

#Funcion get_about_info


def get_about_info():
    info = f"Universidad: {uni}\nEscuela: {escuela}\nCurso: {curso}\nAño: {año}\nGrupo: n/a\nPython: {version}"
    return info

