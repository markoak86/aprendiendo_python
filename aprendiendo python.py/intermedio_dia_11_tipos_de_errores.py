#TIPOS DE ERRORES
#SINTAX ERROR:son errores en la sintaxis del codigo
#print "hola mundo", nos dice el tipo de error y que nos faltan los parentesis
print("hola mundo")

#NAME ERROR:son errores en los nombres de variables
# spanish
#print(spanish), es un name error y nos dice que spanish no esta definido como variable
lenguaje="spanish"
print(lenguaje)

#INDEX ERROR: son errores de indice de las listas
mylist=["python", "java", "php","c++"]
#print(mylist[5]) te dice que es un indice que esta fuera del rango de la rista
print(mylist[2])

#MODULE NOT FOUND: te muestra que el modulo que has intentado importar no se ha encontrado
#import maths, te dice que el modulo con ese nombre no existe
import math

#ATRIBUTE ERROR: son errores de atributos
#print(math.PI) te dice que no existe ese atributo en ese modulo y te sugiere el atributo que se le parece
print(math.pi)

#KEY ERROR: son errores que se producen en un diccionario, en las claves(que es lo que se usa para acceder a los valores)
my_dict={"nombre": "Sara", "apellido": "Garcia", "edad": 38, "trabajo": {"optica","alcampo"}}
#print(my_dict[apelido]), te dice que es una key error y que apelido no se ha definido como key
print(my_dict["apellido"])

#TYPE ERROR: es un error de tipo de dato
#print(mylist["python"]), intentas acceder a una lista con un strig y no con un int
print(mylist[0])

#IMPORT ERROR: son errores a la hora de importar partes de un modulo
#from math import PI, te dice que dentro del modulo no existe ese modulo para importar
from math import pi
print(pi)

#VALUE ERROR: son errores de valor
myInt="10"
print(type(myInt))
myInt= int("10")
print(type(myInt))
#myInt=int("10 años"), cuando estas convertir algo que no se puede comvertir como un texto a int

#ZERO DIVISION ERROR: cuando estamos diviendo un numero entre cero
#mydivision=4/0
#print(mydivision), nos dice que estamos dividiendo un numero entre cero
mydivision=4/2
print(mydivision)