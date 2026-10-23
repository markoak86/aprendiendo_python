#EXCEPCIONES:las excepciones es la forma para detectar errores de codigo en python
#se hace con las palabras reservadas try excep
def sumar(numero1,numero2):
    print(numero1+numero2)

sumar(3,4)
# sumar(3,"4") esto da error porque esta sumando un int con un est
try:
    sumar(5,"4")
except:
    print("esto es un error")#si el try es un error se ejecuta el except

try:
    sumar(9,8)
except:
    print("esto es un error")
else:
    print("esto no es un error")#si se ejecuta el try tambien se ejecuta el else

try:
    sumar(3,"4")
except:
    print("esto es un error")
else:
    print("esto no es un error")
finally:
    print("se ejecuta siempre")#el fanally se ejecuta siempre tanto si hay error como si no

#de la siguiente forma ademas de detectar el herror tambien se puede capturar
try:
    sumar(4,"4")
except Exception as error:
    print(f"el error ha sido capturado como {error}")

#y tambien se pueden filtrar los errores por typos de errores
try:
    sumar(3,"4")
except ValueError as error_value:#filtrar por error de valor y capturar
    print(error_value)
except TypeError as error_type:#filtrar por error de  type y capturar
    print(error_type)

#MODULOS:son como biblotecas, que sirven para utilizar codigo de otros ficheros y asi no tener que duplicar codigo y el copia y pega
#para poder importar ficheros tienen que tener la nomenglatura adecuada
#primero se importa el fichero
import dia_5_funciones

#y despues pues importamos lo que queremos del archivo importado
dia_5_funciones.sara("sara","garcia")

#tambien se puede importan un modulo y cambiarlo de nombre o cambiar de nombre una parte del modulo
import dia_2_listas as que_pasa
print(que_pasa)

#tambien se pueden importar modulos propios de python
import math
print(math.pi)






