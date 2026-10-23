#hacer un procesador de precios con descuentos
#hacer un clousure que devuelva una funcion capapaz de multiplicar un numero por ese factor
def procesador(factor):
    def procesar(numero):
        return numero*factor
    return procesar
print(procesador(4))

#hacer una MAP que le pase a una lista la funcion
precios=[5,12,18,25,30]
precios_transformados=list(map(procesador(10),precios))  	
print(precios_transformados)

#filter para quedarnos solo con los de mas de 150
precios_mayores=list(filter(lambda x: x>150,precios_transformados))
print(precios_mayores)

#reduce para sumar los numeros mayores
from functools import reduce
suma_precios_mayores=reduce(lambda x,y:x+y,precios_mayores)
print(suma_precios_mayores)