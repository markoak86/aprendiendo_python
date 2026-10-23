#tarea1:crear una aplicacion que gestione la lista de equipos de una red
equipos=[{"nombre de equipo":"sara", "ip":"192.168.0.4", "stado":"activo"},
         {"nombre de equipo":"marco", "ip":"192.168.0.10", "stado":"activo"},
         {"nombre de equipo":"aptricia", "ip":"192.168.2.1", "stado":"inactivo"},
         {"nombre de equipo":"alejandra", "ip":"192.168.2.4", "stado":"inactivo"}]



print(equipos[0])
for ordenadores in equipos:
    if ordenadores["stado"]=="activo":
        print(ordenadores)

def equipos_ordenados():
    for ordenadores in equipos:
        print(f"los nombres de los equipos son: {ordenadores["nombre de equipo"]}, y sus ip son: {ordenadores["ip"]}")

print(equipos_ordenados())
ip=str(input("introduce una ip y pulse enter:"))
for ordenadores in equipos:
    if ordenadores["ip"]==ip:
        print("equipo encontrado")
        print(ordenadores)
        break
else:
     print("equipo no encontrado")

menu=["1.ver todos los equipos",
      "2.ver equipos adtivos",
      "3.buscar equipos por ip",
      "4.salir"
      ]
for opcion in menu:
    print(opcion)

