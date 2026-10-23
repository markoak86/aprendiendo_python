#CLASES: Son moldes con atributos y funciones para apartir de ellos crear objetos(instancias) apartir de ellos.
#-1. Para crean con class y el nombre de la clase, con la primera en mayusculas.
class Coche:
    #-2. Se inicializa la clase con el inicializador _init_ y se establecen los argumentos, que son las
    #que se guarda informacion de las instancias de la clase
    def __init__(self,marca, tipo, propietario):
        self.marca=marca
        self.tipo=tipo
        self.propietario=propietario
    
    #-3. Se crean las funciones de la clase, que son las acciones que pueden realizar las instancias.
    def conducir(self):
        print(f" el {self.marca} es un {self.tipo} esta siendo conducido por {self.propietario}")

#-4. Crear instancias a partir de la clase. Las instancias son los objetos reales que se crean a partir del molde de la clase.
my_coche=Coche("hyundai", "deportivo", "Sara")
coche_papa=Coche("toyota", "todoterreno", "Luis")

#-5. Llamamos las funciones
my_coche.conducir()
coche_papa.conducir()

#EJEMPLO DE CLASE: Guerrero.
class Guerrero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.vida=100

    def herida(self,cantidad):
        self.cantidad=cantidad
        self.daño=self.vida - self.cantidad
        print(f"el guerrero {self.nombre} ha sido herido, ha recibido {self.cantidad} daño y le queda {self.daño} de vida")
    def pocion(self, cantidad):
        self.cantidad=cantidad
        self.curacion=self.vida + self.cantidad
        print(f"el guerrero {self.nombre} ha recibido una pocion con {self.cantidad} de curacion y le queda {self.curacion} de vida")

#Creamos las instancias y llamamos a las funciones.
ragnarock=Guerrero("Ragnarock")
sena=Guerrero("Sena")

ragnarock.herida(80)
ragnarock.pocion(60)

sena.herida(20)
sena.pocion(50)
