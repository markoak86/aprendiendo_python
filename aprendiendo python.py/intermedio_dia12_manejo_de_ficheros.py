#MANEJO DE FICHEROS.

#PARA TRABAJAR CON FICHEROS ES MUY UTIL IMPORTAR EL MODULO OS
#TAMBIEN ES MUY UTIL IMPORTAR EL MODULO 
import os

#file1.txt
#1. Abrir fichero: para abrir un fichero hay que usar "open" y se accede a el fichero con la ruta
txt_file1= open("./file1.txt")

#txt_file1= open("./file1.txt")#es el modo por defecto, es como igual que "r"
#txt_file1= open("./file1.txt", "r")# permite leer fichero pero no modificarlo, no borra su contenido al abrirlo
#txt_file1= open("./file1.txt", "w")# permite solo escribir en el fichero, no leerlo y borra su contenido al abrirlo
txt_file1= open("./file1.txt", "r+")# permite leer su contenido y modificarlo, no borra su contenido al abrirlo

#una vez abierto el fichero con los permisos correspondientes podemos pasar a trabajar con el.
print(txt_file1.read(3))#lee caracteres
print(txt_file1.read(20))#lee los siguientes caracteres
print(txt_file1.readline()) #esto lee por linea completa
print(txt_file1.readline())
txt_file1.write("\nestoy escribiendo en un fichero") #asi se escribe en los ficheros

#tambien se puede iterar el fichero por linas
for linea in txt_file1:
    print(linea)

#para cerrar un fichero se hace con .close
txt_file1.close()

#para crear un archivo que no existe hay que usar el w+
texto2=open("texto2.txt", "w+")
texto2.write("hola estas hay")
texto2.seek(0)
print(texto2.read())
texto2.close()


#MANEJO ARCHIVOS JSON
#un archivo JSON es como un diccionario compuesto por clave valor
#para ello hay que importar el modulo JSON
import json

#para crear un archivo json hay que dar 3 pasos
#1.creamos el archivo json
json_file=open("./json_file.json", "w+")

#2.creamos el json el python como un diccionario
json_test={"nombre": "marco",
           "apellido": "marco",
           "edad": 39}

#3. convertimos el diccionario a json con json.dump
json.dump(json_test, json_file)
json_file.seek(0) #el seek mueve el puntero para que python
print(json_file.read())
json_file.close()

#MANEJO DE ARCHIVOS CSV:
#los archivos csv son los archivos excel
#hay que importar el modulo csv
import csv
#creamos el archivo primero
excel=open("./excel.csv", "w+")
#para añadirle las filas se hay que dar dos pasos
#primero se crea el scv para escribir
excel_escrito=csv.writer(excel)
#segundo añadimos cada una de las filas con .writerow
excel_escrito.writerow(["nombre", "apellido", "edad"])
excel_escrito.writerow(["marco", "marco", 39])



