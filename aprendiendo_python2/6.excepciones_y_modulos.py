#EXCEPCIONES: Sirven para poder detectar errores en el codigo, para ello se usa try exept
def suma(numero1, numero2):
    print(numero1 + numero2)
suma(5, 6)

try:
    suma(5,"6")#como no se puede sumar un int con un strig se ejecuta el except
except:
    print("esto es un error")

try:
    suma(5,4)#como no es un error se ejecuta el try (el codigo)
except:
    print("esto es un error")

try:
    suma(5, 5)#como no es un error se ejecuta el codigo y tambien el else
except:
    print("esto es un error")
else:
    print("esto no es un error")

try:
    suma(9,"5")#el finally se ejecuta tanto si hay un error como si no
except:
    print("esto es un error")
else:
    print("esto no es un error")
finally:
    print("me imprimo tanto si es un error como si no")

try:
    suma(7,7)
except:
    print("esto es un error")
else:
    print("esto no es un error")
finally:
    print("esto se imprime tanto si es un error como si no")

#MODULOS: Son como las librerias en otros lenguajes, son archivos con codigo de python creado por otros para poder usarlo
#y no tener que volver el codigo que ya esta escrito. Hay modulos que son propios de python.

#-1. Hay que importar los modulos con import
import math as matematicas

#una vez importado el modulo, ya se puede usar todo lo que hay en el
print(matematicas.pi)
print(matematicas.sqrt(25))


