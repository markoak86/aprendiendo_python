#LISTAS: se escriben entre corchetes y con los elementos seperados por comas
my_lista=["Marco", 40, 1.90]
lenguajes=["python", "C", "java script", "php"]
print(my_lista)
print(my_lista.index(40))#te dice el indice del elemento
print(my_lista[1])#te dice el elemento por indice
print(len(lenguajes))#te dice el numero de elementos de la lista
print(lenguajes.count("php"))#te dice el numero de veces que aparece un elemento
#añadir elementos en listas
my_lista.append("casado")#añade al final
lenguajes.insert(0, "sql")#inserta donde tu quieras
print(my_lista)
print(lenguajes)
my_lista[0]="Mateo"#sustitulle elemento
print(my_lista)
#eleminar elementos
my_lista.remove(40)#elimina el elemento por nombre
del(lenguajes[0])#elimina elemento por indice
print(my_lista)
print(lenguajes)
estado_civil=my_lista.pop(2)#desapila el elemento y lo guarda en una variable
print(my_lista)
print(estado_civil)
#ordenar listas
lenguajes.reverse()#invierte el orden
print(lenguajes)
lenguajes.sort()#ordena la lista en orden alfabetico
print(lenguajes)
#copiar listas
my_new_list=my_lista.copy()
print(my_new_list)

#TUPLAS: son como las listas, pero su cotenido es inmutable, no se pueden ni añadir ni eliminar elementos. Van entre parensis
my_tupla=("Julia", 4, 75.4, "estudiante")
my_otra_tupla=(24, 65, 90, 76)
suma_tuplas=my_tupla + my_otra_tupla
print(suma_tuplas)
print(my_tupla.index("estudiante"))
print(my_otra_tupla[2])

#SET: los set son como una lista, que estan desordenadas y que no se pueden repetir datos. Van entre llaves
my_set={"Sara", 38, 1.53, "optica", "Sara", 38 }
print(my_set)#solo aparece un 38 y un Sara y desordenado
print(len(my_set))

#DICCIONARIO: es una estructura de datos que se organizan en pares clave: valor. Va entre llaves, la clave y el valor se separa con : y los pares se separan por ,
my_diccionario={"nombre": "Patricia", "edad": 50, "altura": 1.60, "trabajo": "programadora"}
#para ver llaves, valores y los items
print(my_diccionario.keys())
print(my_diccionario.values())
print(my_diccionario.items())
#para modificar algun elemento
my_diccionario["trabajo"]="informatica"
print(my_diccionario)
#para añadir un elemento
my_diccionario["hijos"]=1
print(my_diccionario)
#para desapilar y guardar un valor en una variable
edad=my_diccionario.pop("edad")
print(edad)
print(my_diccionario)
#para buscar elementos por claves en los diccionarios
print("altura" in my_diccionario)
