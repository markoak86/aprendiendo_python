#FUNCIONES: son bloques de codigo que se sirven para poder reutilizarlo varias veces ganando tiempo y minimizando errores.
#Para escribir una funcion hay que seguir dos pasos: primero definirla y despues llamarla para ejecutarla
def my_funcion_sin_argumentos():#definicion
    print("esta es mi funcion sin argumentos")
my_funcion_sin_argumentos()#llamada

def nombre_completo(nombre,apellido1,apellido2):#funcion con argumentos
    print(f"mi nombre es {nombre}, mi primer apellido es {apellido1} y mi segundo apellido es {apellido2}")
nombre_completo("marco","marco","quiros")
 
def sara(nombre, apellido, profesion="optica"):#funcion con argumentos por defecto
    print(f"hola soy {nombre} {apellido} y soy {profesion}")
sara("Sara", "Garcia")
sara("Sara", "Garcia", "jefa")

def persona(*argumentos):#funcion con argumentos variables
    print(f"soy {argumentos}")
persona("marco", "marco", "quiros")

def funcion_suma(numero1, numero2):#funcion con retorno de argumentos para guardar en una variable, una funcion sin retorno devuelve NONE
    return(numero1 + numero2)
resultado=funcion_suma(43,33)
print(resultado)