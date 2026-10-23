#tipos de datos y operaciones
nombre_de_servidor="servdor web"
ram_actual= 8
precio_ram=35.5
coste_total= (ram_actual*2)*precio_ram
print(coste_total)

#listas de control:listas,tuplas,sets y diccionarios
servicios=["http","ssh","fpt"]
servicios.append("dns")
print(servicios)
servicios.remove("fpt")
print(servicios)

servidor_local={"ip":"192.168.4.2", "so":"linux","estado":True}
print(servidor_local["ip"])

#if, elif, else
#crear un programa que pida una ip por teclado
ip= str(input("introduzca una ip y pulse enter:"))
if ip=="127.0.0.1":
    print("este es el local host")
elif ip.startswith("192."):
    print("es una ip privada")
else:
    print("es una ip publica")    

#recorrer la lista de puertos para ver si el pueto esta abierto (80,443) o si es un puerto de servicio adtivo (el resto)
lista_puertos=[21, 22, 25, 80, 443] 
for puertos in lista_puertos:
    if puertos==80 or puertos==443:
        print("puerto web abierto")
    else:
        print("puerto de servicio activo")

#EJERCICIO 2:
#crear un diccionario donde la clave es la ip y el valor el hostname
nodos={"192.168.1.10": "SERV-WEB-01",
       "192.168.1.11": "srv-db-02",
       "10.0.0.5": "Router-Principal",
       "192.168.1.50": "PC-Usuario-01",
       "8.8.8.8": "DNS Google"}

#las listas de ips que el firewall ha marcado como sospechosas son:
ips_bloqueadas=["10.0.0.5", "8.8.8.8"]
red_local=[]

#añade a la lista red local las ips que empizen por 192.
ips=nodos.keys()
print(ips)
for ips, nombres in nodos.items():
    if ips.startswith("192."):
        print("añadendo a la red local")
        red_local.append(f"{ips}, {nombres.upper()}")
print(red_local)

#seguridad:si al recorrer el diccionario se encuentra una ip de las ips bloqueadas  imprimir mensaje de alerta
for ips in nodos.keys():
    if ips in ips_bloqueadas:
        print(f"SEGURIDAD: El equipo {nombres.upper()} con ip {ips} esta bajo vigilancia")

#para saber cuantos elementos tienen la lista de red local
print(len(red_local))

        