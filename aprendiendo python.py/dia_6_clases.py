#CLASES: las clases sirven para crear objetos, se crean con class y la primera letra va en mayuscula
class Coche:
    #despues se utiliza el constructor de clase _init_, que es el que inicializa los atributos
    #los atributos son las variables que guardan informacion del objeto
    def __init__(self, marca, modelo):
        self.marca= marca
        self.modelo= modelo #self hace referencia al objeto actual
        #las clases ademas de atributos tienen metodos, que son las funciones que definen que puede hacer el objeto
    def conducir(self):
            print(f"conduciendo el {self.marca}, de {self.modelo}")
#las instancias es el objeto real creado apartir del molde de la clase
mi_coche= Coche("toyota", "corola")
mi_coche.conducir()
#ejemplo de clase Guerrero
class Guerrero:
    def __init__(self, nombre):
        self.nombre= nombre
        self.vida= 100
    def estado(self):
            print(f"el nombre de mi guerreo es {self.nombre} y tiene {self.vida} de vida")
    def recibir_daño(self,cantidad):
          self.cantidad=self.vida-cantidad
          
          print(f"{self.nombre}, recibio {cantidad} de daño y el queda {self.cantidad} de vida")
    def curar_daño(self,salud):
         self.salud=self.cantidad+salud
         print(f"el guerrero {self.nombre} ha recibido {salud} de vida, se ha curado, y ahora tiene la {self.salud} de vida")
mi_guerrero= Guerrero("ragnar")
mi_guerrero.estado()
#ha recibido 30 de daño
mi_guerrero.recibir_daño(30)
mi_guerrero.curar_daño(20)



    
          