#paso 1: crear una clase llamada servidor:
class Servidor:
    def __init__(self, nombre, ip, sistema_operativo):
        self.nombre=nombre
        self.ip=ip
        self.sistema_operativo=sistema_operativo
        self.estado="Adtivo"

#crear un diccionario vacio llamado inventario que iremos llenando despues
inventario={}

#importar un modulo externo
import datetime
import os

#crear un bucle con el menu y con un detector de errores para que en caso de fallo se muestre un mensaje amigable
while True:
    
    try:
        print("MENU")
        print("1.añadir")
        print("2.listar")
        print("3.salir")
        opcion=int(input("introduzca un numero y pulse enter:"))
    except ValueError:
        print("por favor, introduzca un numero valido")
    #creamos un condicional para que si pulsamos 3 se salga del bucle
    if opcion==3:
        print("saliendo del sistema")
        break
    elif opcion==1:#creamos un condicional para ir rellenando cada objeto de la clase
        nombre=str(input("introduzca nombre de servidor y pulse enter:"))
        ip=str(input("introduzca ip y pulse enter:"))
        sistema_operativo=str(input("introduzca sistema operativo y pulse enter:"))
#luego creamos el objeto dentro de la clase 
        nuevo_servidor= Servidor(nombre,ip,sistema_operativo)
#guardamos cada objeto de la clase dentro del diccionario inventario
        inventario[nombre]=nuevo_servidor
        ahora=datetime.datetime.now()
        print(f"el servidor {nombre} se ha guardado con exito a las {ahora}")
        input("pulse enter para continuar")
        #aqui creamos el condicional para la opcion 2
    elif opcion==2:
        print("INVENTARIO DE SERVIDORES")
        if not inventario:#si no hay nada dentro del diccionario que nos avise
            print("el inventario esta vacio")
        else:
            for s in inventario.values():#bucle para que acceda a los valores de cada elemento del diccionario
                print(f"SERVIDOR: {s.nombre}")
                print(f"IP: {s.ip}")
                print(f"SISTEMA OPERATIVO: {s.sistema_operativo}")
            input("pulse enter para volver al menu")
    


    
   
        





