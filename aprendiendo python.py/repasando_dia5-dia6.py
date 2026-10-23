#repaso de funciones y clases
#FUNCIONES:
#escaner de seguridad con funciones
puertos_detectados=[22, 80, 443, 21, 3306, 23, 25]

def evaluar_seguridad(puertos_detectados):
    puertos_criticos=[]
    for puertos in puertos_detectados:
        if puertos==21 or puertos==23 or puertos==25:
            puertos_criticos.append(puertos)
    return puertos_criticos

resultados_finales= evaluar_seguridad(puertos_detectados)

if len(resultados_finales)>0:
    print(f"RIESGO ALTO: CIERRA LOS PUERTOS {resultados_finales}")
else:
    print("SEGURIDAD CORRECTA: NO HAY PUERTOS CRITICOS")

#gestor de nodos
#el diccionario es la base de datos
servidores={"Web":"192.168.1.10",
            "Proxy":"192.168.1.50",
            "Correo":"10.0.0.5",
            "DNS":"8.8.8.8"}


ip=servidores.values()
print(ip)
#funcion de validacion:sirve para analizar los ip,si empizan por 192. es servidor local, si no, es remoto
def analizar_nodo(ip):
    
  
        if ip.startswith("192."):
            return("local")
        else:
            return("remoto")
        
#logica para la interactividad
#creamos un input para analizar que el usuario nos meta el nombre del servidor por consola
servidor_consulta=str(input("¿que servidor quieres consultar?introducelo y pulsa enter:"))

if servidor_consulta in servidores:
    ip=servidores[servidor_consulta]
    analizar_nodo(ip)
    print(f"el servidor {servidor_consulta},con ip {ip} esta en la ubicacion {analizar_nodo(ip)}")
else:
    print("ERROR:EL SERVIDOR NO EXISTE EN LA BASE DE DATOS")

#CLASES:
#defdinir una clase que se llama servidor con su nombre, ip y un metodo para analizarse a si mismo
class Servidor:
    def __init__(self, nombre, ip):
        self.nombre= nombre
        self.ip= ip

    def __str__(self):
        return(f"el servidor {self.nombre}, tiene el ip {self.ip}")
    
    
    def analizar(self):
        if self.ip.startswith("192."):
            return("Red Local")
        else:
            return("Red Externa")
        
srv1= Servidor("Web", "192.168.1.10")
srv2= Servidor("DNS","8.8.8.8")

print(srv1)
print(srv2)
print(srv1.analizar())
print(srv2.analizar())



