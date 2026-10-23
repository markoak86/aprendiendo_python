#LAMBDA:son funciones sin nombre que se definen con la palabra lambda en una sola linea de codigo
#sirven para tareas sencillas y rapidas que no se van a reutilizar
sum_values=lambda value1,value2:print(value1+value2) #las lambda hay que guardarlas en una variable para poder "llamarlas"
sum_values(5,7)
#el equivalente en funcion normal seria:
def sum_values_normal(value1, value2):
    print(value1+value2)

sum_values_normal(8,7)

#FUNCIONES DE ORDEN SUPERIOR:son aquellas que tienen dentro otra funcion,se las pasa una funcion como su fuese una funcion cualquiera

def sum_one(value):
    return value +1

def sum_values_and_one(value1, value2, sum_one):
    return(value1+value2+sum_one)

print(sum_one(4))
print(sum_values_and_one(3,4,8))

#FUNCIONES DE CIERRE CLOSURES:es una funcion que dentro lleva una funcion, pero que ademas devuelve una funcion
def crear_saludador(saludo):
    def saludar(nombre):
        return f"{saludo}", {nombre}
    return saludar

#creamos una instacia del clousure
hola_en_espanol=crear_saludador("HOLA")
hola_en_ingles=crear_saludador("HELLO")

print(hola_en_ingles("LUCI"))
print(hola_en_espanol("ANA"))

#MAP: se usa para aplicar una misma operacion a cada elemento de una lista
numeros=[1, 2, 3, 4]
#multiplicamos cada numero por dos
resultado=list(map(lambda x: x*2, numeros))
print(resultado)

#FILTER: se usa para filtrar elementos de una lista que cumplen una condicion, la funcion que le pasas tiene que devolver TRUE O FALSE.
numeros=[4,5,6,7]
pares=list(filter(lambda x: x%2==0, numeros))
print(pares)

#REDUCE: coje todos los elementos de una lista y los convina para devolver un solo valor (como una suma total o un producto)
#para usar reduce primero hay que importarlo de functools
from functools import reduce
numeros=[1,2,3,4,5,6]
resultado_suma=reduce(lambda x,y:x+y,numeros)
print(resultado_suma)
