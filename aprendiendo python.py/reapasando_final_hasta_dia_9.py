#SISTEMA DE GESTIÓN DE BIBLIOTECA PERSONAL
#Paso1: la clase y las fechas
import datetime
from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, fecha_de_publicacion,categoria):
        self.titulo=titulo
        self.autor=autor
        self.fecha_de_publicacion=datetime.strptime(fecha_de_publicacion, "%d/%m/%Y").date()
        self.catergoria="clasico" or "contemporaneo"

    def __str__(self):
        return(f"libro: {self.titulo}, autor: {self.autor}, con fecha de publicacion: {self.fecha_de_publicacion}")
  

mi_libro=Libro("don quijote", "cervantes", "4/4/1548", "clasico")
print(mi_libro)

#Paso 2:listas y diccionarios
biblioteca_total=[]
categorias={}
#creamos las llaves del diccionario que dentro contienen una lista
categorias["clasicos"]=[]
categorias["contemporaneos"]=[]

#añadir el objeto mi libro a la biblioteca total y las categorias dentro de la llave diccionario
biblioteca_total.append(mi_libro)
categorias["clasicos"].append(mi_libro)

print(biblioteca_total)
print(categorias["clasicos"])

#Paso 3:Bucles y las Extensiones
#crear un menu con varias opciones: añadir, libro y salir
 
while True:
    print("MENU")
    print("1.Añadir libro")
    print("2.Listar libros")
    print("3.Salir")
    print("4.libros modernos")
    
    opcion=input("introduce una opcion y pulsa enter:")
        
    
    if opcion=="1":
       
        titulo=input("introduce titulo y pulsa enter:")
        autor=input("introduce el nombre del autor y pulsa enter:")
        fecha_de_publicacion=input("introduce la fecha de publicacion y pulsa enter:")
        categoria=input("introduce categoria: clasico o contemporaneo")
#creamos un objeto con los datos introducidos
        nuevo_libro= Libro(titulo, autor, fecha_de_publicacion,categoria)
            #y si sale bien, ese objeto le añadimos a la lista biblioteca
        biblioteca_total.append(nuevo_libro)
        if nuevo_libro.catergoria=="clasico":
            categorias["clasicos"].append(nuevo_libro)
            print(categorias["clasicos"])
        else:
            categorias["contemporaneos"].append(nuevo_libro)
            print(categorias["contemporaneos"])

    elif opcion=="2":#creamos un bucle for para que vaya pasando por cada elemento de la lista
        print("lista de libros en la biblioteca")
        for libro in biblioteca_total:
            print(libro)
    elif opcion=="3":
        print("saliendo del sistema")
        break
    #Paso 4: list comprehesion
    #crear una opcion cuatro con la list compresion para filtrar solo los libros modernos,posteriores al 2000
    elif opcion=="4":
        print("buscando libros modernos")
        libros_modernos=[mi_libro.titulo for mi_libro in biblioteca_total if mi_libro.fecha_de_publicacion.year>2000]
        print(f"los libros publicados despues del 2000 son: {libros_modernos}")
    else:
        ("opcion no valida, intentalo de nuevo")


    

    
    