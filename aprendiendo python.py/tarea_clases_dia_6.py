#crear una clase llamada Servidor
class Servidor:
    def __init__(self,nombre, ip):
        self.nombre= nombre
        self.ip= ip
        self.uso_cpu=0
    def actualizar_cpu(self,actualizacion):
        self.actualizacion=0+actualizacion
        print(f"el uso de cpu es {self.actualizacion}")
    
    def estado_servidor(self):
        
        
        print(f"el nombre del servidor es {self.nombre} y su direccion ip es {self.ip}")
    def estado_cpu(self, uso_cpu):
        self.uso_cpu=uso_cpu
        uso_cpu=int(input("introduce el uso de cpu y pulsa enter:"))

        if self.uso_cpu>80:
            print("ALERTA")
        else:
            print("Ok")
        
s_ventas= Servidor("ventas","192.168.2.6")
s_clientes= Servidor("clientes","192.168.4.2")
s_compras= Servidor("compras","192.168.7.3")
s_ventas.actualizar_cpu(80)
s_ventas.estado_cpu(90)
s_ventas.estado_servidor()

inventario= [s_ventas,s_clientes,s_compras]

for servidores in inventario:
    print(servidores.estado_servidor())



