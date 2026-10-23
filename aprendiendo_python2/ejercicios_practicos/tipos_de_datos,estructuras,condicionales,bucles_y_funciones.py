#GESTOR DE SERVIDORES.

#1. Estructuras de datos
#-diccionario
servidores={"srv-web":{"ip":"192.168.1.23", "estado":False, "servicios":["http, https"]}, "srv-db":{"ip":"192.168.2.24", "estado": True, "servicios":["ftp, ftps"]}}
#-tupla (no se puede modificar)
ip_permitidas=("192.168.1.23", "192.158.6.98")
#-set (no admite elementos duplicados)
servicios_criticos={"ssh", "dns", "database"}

#2.funciones:
#-funcion para mostrar los servidores y mostrar su estado
def mostrar_servidores():
    for servidor in servidores:
        nombre_servidor=servidor
        estado_servidor=servidores[servidor]["estado"]
        if estado_servidor==True:
            print(f"el servidor {nombre_servidor} esta online")
        else:
            print(f"el servidor {nombre_servidor} esta offline")

#funcion para determinar si la ip es segura o no
mostrar_servidores()
def verificar_seguridad(ip_verificada=input("introduce una ip y pulsa enter:")):
    if ip_verificada in ip_permitidas:
        print("la ip es segura")
    else:
        print("la ip no es segura")
verificar_seguridad()

#funcion para determinar si algun servidores inactivos tiene algun servicio critico
def alerta_critica():
    for servidor in servidores:
        estado_servidor=servidores[servidor]["estado"]
        if estado_servidor==False:
            for servicio_servidor_inactivo in servidores[servidor]["servicios"]:
                if servicio_servidor_inactivo in servicios_criticos:
                    print("ALERTA:SERVIDOR CON SERVICIO CRITICO")
                else:
                    print("servidor sin servicio critico")
        else:
            print("servidor activo")

alerta_critica()