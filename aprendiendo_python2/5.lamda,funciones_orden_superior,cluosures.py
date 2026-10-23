#LAMDA: son funciones que se definen en una sola linea, se utilizan cuando las funciones que se quieren definir son cortas y sencillas y que no
#se van a reutilizar.
#Las lamdas se almacenan en variables y la funcion lamda se llama con el nombre de la variable.
suma_numeros=lambda numero1,numero2,numero3: print(f"el resultado es {numero1+numero2+numero3}")
suma_numeros(6,5,7)

#la misma funcion:
def suma_numeros_normal(numero1,numero2,numero3):
    print(f"el resultado de suma numeros normar es {numero1 + numero2 + numero3}")
suma_numeros_normal(8,9,6)

#FUNCIONES DE ORDEN SUPERIOR: son funciones con otra funcion dentro, se las pasa una funcion como si fuera un argumeto mas.
def sum_one(value):
    return value + 1
#-funcion con funcion dentro:
def sum_value_one(value1, sum_one):
    print(value1 + sum_one)

sum_value_one(8,sum_one(3))

def multiplica_por_dos(num):
    return num * 2

def suma_y_multiplica(value, multiplica_por_dos):
    print(value + multiplica_por_dos)

suma_y_multiplica(8,multiplica_por_dos(4))

#FUNCION DE CIERRE, CLOUSURES: son funciones que dentro lleva otra funcion, pero que ademas devuelve otra funcion
def crear_saludador(saludo):
    def saludar(nombre):
        return f"{saludo} {nombre}"
    return saludar

#-una vez creada la funcion de cierre hay que crear estancias de las clousures para poder llamarlas
saludar_en_ingles=crear_saludador("HELLO")
print(saludar_en_ingles("JULIA"))

saludar_en_español=crear_saludador("HOLA")
print(saludar_en_español("SARA"))

#MAP: se usa para pasar una operacion a cada elemento de una lista, la operacion se pasa como una funcion lambda.
numeros=[1,2,3,4,5,6]
multiplica_por_tres=list(map(lambda numero:  numero *3, numeros))
print(multiplica_por_tres)

#FILTER: sirve para filtrar los elementos que de una lista que cumplen una condicion, la condicion se pasa como una funcion lambda tiene que devolver true o false
divisible_entre_dos=list(filter(lambda numero: numero%2==0, numeros))
print(divisible_entre_dos)

#REDUCE: sirve para convinar todos los elementos de una lista, hacer una operacion sobre ellos y mostrar su resultado: para ello,
#hay que descarg,ar reduce del modulo functools y la operacion se pasa como una lambda
num_para_sumar=[8,9,56,41]
from functools import reduce
suma_lista=reduce(lambda x, y: x+ y, num_para_sumar)
print(suma_lista)