#EL MONITOR DE CONEXIONES DE RED (PING SIMULATOR): SCRIPT PARA COMPROBAR LA CONECTIVIDAD DE LOS SERVIDORES. SI UN IP NO RESPONDE O TIENE UN FORMATO
#INCORRECTO CAPTURAR EL ERROR

#-1. Definir la clase servidor:
class Servidor:
    def __init__(self, nombre, ip, servicios):
        self.nombre=nombre
        self.ip=ip
        self.servicios=servicios
        self.estado= "Desconocido"

    #-definir el metodo de la clase para simular el ping.
    def simular_ping (self, ip_destino):
        #-Crear la captura de errores para detectar la ip 0.0.0.0 y que salte un value error.
       if ip_destino=="0.0.0.0":
        raise ValueError ("ip de destino no valida (0.0.0.0 no enrutable)")

        #-definir el condicional comprobar la ip destino del ping y modificar le estado del servidor
        if ip_destino==self.ip:
            self.estado="ONLINE"
            print(f"el servidor {self.nombre}, con una ip {self.ip} tiene un estado {self.estado}")
        else:
            self.estado="OUTLINE"
            print(f"el servidor {self.nombre}, con una ip {self.ip} tiene un estado {self.estado}")

#-2. Crear una lista con las instancias (objetos) de la clase servidor
servidor_web= Servidor("web", "192.168.1.40", ["http","https"])
servidor_DataBase= Servidor("Base de datos", "223.65.3.4", ["sql", "mysql"])
servidores=[servidor_web, servidor_DataBase]

#-3. Crear una lista con las ip para hacer ping
ips_destino=["192.168.1.40", "0.0.0.0", "80.80.80.80"]

#-4. Crear un bucle que pase por cada servidor
for servidor in servidores:
   #crear otro bucle que pase por cada ip en la lista de ip de destinos
   for ip in ips_destino:
      try:
        servidor.simular_ping(ip)
      except ValueError as error:
         print(f"ALERTA: En {servidor.nombre}: {error}")


            