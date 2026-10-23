#EL MODULO SYS: modulo que sirve para interactuar con el sistema operativo, para capturar exepciones y terminar el flujo de informacion
import sys

#sys.argv sirve para pasar argumentos al programa por la terminal

def obterner_parametros():#la funcion revisa si el usu pasa la ip y el nombre, si esta bien lo devuelve, si no cierra el programa
    nombre_programa=sys.argv[0] #este es el nombre del script, pero no es necesario
    if len(sys.argv) < 3: #el programa para checkear el servidor, la ip y el nombre
        print("error: faltan datos")
        print("uso correcto: python.py ip y nombre_de_servidor")
        sys.exit(1) #cerramos el flujo porque no podemos seguir sin datos
    #si llegamos aqui, es que hay argumentos suficientes 
    ip_servidor=sys.argv[1]
    nombre_servidor=sys.argv[2]
    return ip_servidor, nombre_servidor

#aqui empieza el programa, llamamos a nuestra funcion y la guardamos los resultados en una variable
ip, nombre=obterner_parametros()
print(f"configurando el servidor {nombre}, con ip {ip}")

#MANEJO DE ARCHIVOS: como .txt, .csv, .conf
# primero hay que abrir el archivo con with open,w (with sirve para que se cierre automaticamente aunque haya un error)
#ESCRITURA DE ARCHIVOS
with open("servidores.txt", "w") as archivo:
    archivo.write("192.168.4.2\n")
    archivo.write("192.8.3.6\n")

#LECTURA DE ARCHIVOS
with open("servidores.txt", "r") as archivo:
   
    for linea in archivo:
        print(f"HACIENDO PING A: {linea.strip()}")
