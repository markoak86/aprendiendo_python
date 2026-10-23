#ejercicio 1: gestion de inventario.
servidores=["web","bases de datos","correo"]
servidores_con_ip={"web":"192.168.1.8", "bases de datos":"192.168.1.3", "correo":"192.168.1.5"}
sistemas_operativos=set(["debian", "ubuntu", "windows", "centOS"])


for nombre,ip in servidores_con_ip.items():
    print(f"el servidor: {nombre} con ip: {ip}")
    if nombre=="correo":
        print(f"el servidor {nombre} requiere MANTENIMIENTO NECESARIO")

#ejercicio 2: automatizacion de usuarios.
class Usuario:
    def __init__(self,nombre,rol):
        self.nombre=nombre
        self.rol=rol
usu_marco= Usuario("Marco","administrador")
usu_sara= Usuario("Sara", "invitado")
usu_patricia= Usuario("Patricia", "tecnico")
lista_de_usuarios=[usu_marco, usu_patricia, usu_sara]
        
    