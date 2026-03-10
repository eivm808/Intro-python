#Universidad: Instituto Tecnológico de Costa Rica
#Escuela: Ingeniería en Computadores
#Curso: Introducción a la Programación
#Año: 2026
#Grupo: n/a
#Versión de Python: 3.14.3

#Estudiantes: Brenda y Ericka Villalobos
#Título: Introducción a Python
#Descripción: Exploración de 4 bibliotecas de Python (math, random, datetime, os) con ejemplos documentados, y uso de la biblioteca personalizada tec_info.
#Versión del programa: 1.0
#Requerimientos del sistema: Python 3.8 o superior

#--------------------------------------------Importaciones--------------------------------------------------------
import math

#Funcion 1: Calcular la raiz cuadrada de un numero.

print("Raiz cuadrada: ", math.sqrt(16))

#Funcion 2: Calcular el Máximo común divisor de numero y numero

print ("MCD de numero y numero: ", math.gcd(20, 10)) 

#--------------------------------------------------------------------------------
import random

#Funcion 1: Escojer un entero aleatorio entre 1 y 10

print("Numero random entre 1 y 10: ", random.randint(1,10))

#Funcion 2: Seleccionar un elemento al azar 

frutas = ["manzana", "banana","cereza"]
print("Fruta random: ", random.choice(frutas))

#--------------------------------------------------------------------------------
import datetime
import os

#--------------------------------------------------------------------------------

import string 

#Funcion 1: Comprueba la longitud de la cadena.

print("Cuantas letras?", len("Santiago"))

#Funcion 2: Capitaliza cada palabra.

print("Capitalizar: ","hola mundo".title())

#-------------------------------------------------------------------------------

import statistics

#Funcion 1: Calcula la media aritmetica de un conjunto de datos

datos = [10, 20, 20, 40, 50]
print("Media Aritmetica: ",statistics.mean(datos))

#Funcion 2: Calcula la mediana de un conjunto de datos

data = [10, 30, 50 , 70, 90]
print("Mediana: ",statistics.median(data))

#-------------------------------------------------------------------------------

import calendar

#Funcion 1: Generacion de calendario de texto para un mes

print("Calendario a Texto: ")
print(calendar.month(2026, 3))

#Funcion 2: Verificar si un año es bisiesto

print("¿2026 es un año bisiesto?", calendar.isleap(2026))

#-------------------------------------------------------------------------------

import time

#Funcion 1: Mostrar la hora actual en timestamp

ahora = time.time()
print("Timestamp actual:", ahora)

#Funcion 2: Pausa la ehecucuion durante el numero de segundos indicado.

print("Tiempo de respuesta de dos segundos",time.sleep(2))

#--------------------------------------------------------------------------------

import collections

#Funcion 1: Cuenta la frecuencia de elementos en un iterable

from collections import Counter

c = Counter("banana")
print("Cantidad de elementos: ",c)               #Counter({'a': 3, 'n' = 2, 'b' = 1})
print("Elemento mas comun: ", c.most_common(1)) # [('a', 3)]

#Funcion 2: Crear subclases de tuplas

from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'edad'])
p = Persona(nombre="Ana", edad=30)
print(p.nombre)  # Ana
print(p[1])      # 30

#----------------------------------------------------------------------------------

