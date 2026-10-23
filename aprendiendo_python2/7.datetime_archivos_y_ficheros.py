#DATETIME: este modulo sirve para trabajar con fechar y hora.
import datetime
hoy=datetime.datetime.now() #para registrar la fecha actual
print(hoy)
dia_puesto_por_mi=datetime.datetime(2000,4,4)
print(dia_puesto_por_mi)

#para dividir la fecha se hace de la siguiente forma:
from datetime import datetime

año=datetime.now().year
mes=datetime.now().month
dia=datetime.now().day
def fecha_completa():
    print(año)
    print(mes)
    print(dia)
fecha_completa()

#timestampt es un formato de fecha y hora que las computadoras entienden independientemente de la zona horaria
timestamp=datetime.now().timestamp()
print(timestamp)

#para trabajar con periodos de tiempo el modulo timedelta
from datetime import timedelta
periodo1=timedelta(weeks= 52, days= 365)
periodo2=timedelta(weeks=26, days=134)
print(periodo1)
print(periodo2)

#MANEJO DE ARCHIVOS:
#-1.lo primero es descargar el modulo os
#-2. lo segungo que hay que hacer es crear el archivo con open,se pone la ruta donde se alojara el archivo
# y se le asigna los permisos que se quiera, en este caso w+, y guardarlo en una variable.
import os
archivo_texto=open("./file1.txt", "w+")
#asi se escribe en un fichero:
archivo_texto.write("este es mi primer archivo de texto\ny estoy escribiendo varias lineas en él\npara despues poder leerlo")
#para leer el archivo  lo primero que hay que hacer es llevar el puntero al principio del archivo con seek
#porque si no el puntero esta al final y la lectura es apartir del punter y despues hay que imprimirle:
archivo_texto.seek(0)
print(archivo_texto.read())
#para leer lineas:
archivo_texto.seek(0)
print(archivo_texto.readlines(1))
print(archivo_texto.readlines(1))
#para leer caracteres:
archivo_texto.seek(0)
print(archivo_texto.readline(8))#lee 8 caractares
archivo_texto.seek(0)
print(archivo_texto.read(8))#tambien lee 8 caracteres
#POR ULTIMO Y MUY IMPORTANTE, HAY QUE CERRAR EL ARCHIVO.
archivo_texto.close()

#MANEJO DE ARCHIVOS JSON: LOS ARCHIVOS JSON TIENEN LA MISMA ESTRUCTURA QUE UN DICCIONARIO EN PYTHON
#-1. Hay que importar el modulo json
import json
#-3. primero hay que crear el archivo json como cualquier otro, con ruta y permisos y guardandolo en una variable
archivo_json=open("./archivo_jason.json", "w+")

#-2.primero creamos un diccionario para despues poder convertirlo en un archivo json con json.dump,
#poniendo entre parentesis el nombre del diccionario y el nombre de la variable del archivo json
marco={"nombre": "Marco",
       "apellido": "Marco",
       "edad": 40,
       "altura": 1.90}
json.dump(marco, archivo_json)
#una vez hecho esto ya trabajamos con el archivo json como con otro archivo
archivo_json.seek(0)
print(archivo_json.read())
archivo_json.seek(0)
print(archivo_json.readlines(1))
#IMPORTANTE:CERRAR ARCHIVO
archivo_json.close()

#MANEJO DE ARCHIVOS CSV: LOS ARCHIVOS CSV SON EXCEL
#-1. Hay que importar el modulo csv
import csv
#-2. Despues se crea el archivo csv igual que en los casos anteriores
excell=open("./excell.csv", "w+")
#-3. Con los archivos csv para añadir linear hay que llevar acabo dos pasos:
excell_escrito=csv.writer(excell)
excell_escrito.writerow(["nombre", "apellido", "edad"])#las lineas se escriben como listas
excell_escrito.writerow(["Marco", "Marco", 40])

excell.seek(0)
print(excell.read())



    