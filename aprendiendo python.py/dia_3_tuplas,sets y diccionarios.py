#TUPLAS: las tuplas son como las listas pero su contenido es inmutable
#definición de tuplas entre parentesis y con sus elementos separados con comas, tambien formalmente
my_new_tuple= tuple()
my_tuple= ("calimero", 1.39, "perrito", 5, "dartañan", -1)
print(my_new_tuple)
print(my_tuple)
print(type(my_new_tuple))
print(type(my_tuple))
#operaciones que se pueden hacer con tuplas
print(my_tuple.index("calimero"))
print(my_tuple.count(5))
my_tuple2=(23, 3, 45, 67)
sume_tuple= my_tuple+my_tuple2
print(sume_tuple)
print(len(sume_tuple))
#con las tuplas no se puede ni añadir, ni insertar, ni tampoco eliminar elementos
#la unica forma de modificar una tupla es convertirla en lista y volverla a convertirla en tupla
my_tuple2= list(my_tuple2)
print(type(my_tuple2))
my_tuple2[2]="cuarenta y cinco"
print(my_tuple2)
my_tuple2= tuple(my_tuple2)
print(type(my_tuple2))
#my_tuple2[2]= 45 ahora esto da error
#para eliminar una tupla la unica forma es eliminar la tupla por completo con del
del my_tuple2
#print(my_tuple2) esto da error porque my_tuple2 ya no existe

#SETS: los sets son como listas pero que no estan ordenadas y que no admiten elementos repetidos
#se definen entre {} y con los elementos separados por comas o formalmente
my_new_set= set()
my_set={"maravilla,", 67, "cerro", 67}
print(my_new_set)
print(my_set)#vemos que solo se imprime un 67
print(len(my_set))# y que solo cuenta un 67
#se pueden añadir elementos al set
my_set.add("camello")
print(my_set)
#tambien se puede ver si un elemento esta en el set o no
print("camello" in my_set)
print("castillo" in my_set)
#se pueden unir set
my_set2={54, 86, 97, 33, 44}
my_set3= my_set2.union(my_set)
print(my_set2)
print(my_set3)
#se pueden eliminar elementos, limpriar el set y eliminar el set entero
my_set.remove(67)
print(my_set)
my_set.clear()
print(my_set)
del my_set
#print(my_set) esto no lo permite porque my_set ya no existe

#DICCIONARIOS: los diccionarios son como listas pero cada elemento esta formado por clave: valor
#se define entre {} y pero con la key y el value separados por : o formalmente
m_dic= dict()
print(type(m_dic))
my_dict={"nombre": "Sara", "apellido": "Garcia", "edad": 38, "trabajo": {"optica","alcampo"}}
print(my_dict)
print(len(my_dict))#cada elemento es una key y su value
#puedo cambiar un value
my_dict["edad"]= 35
print(my_dict)
#para buscar un value
print(my_dict["trabajo"])
#para ver las claves o los valores o los items
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
#para eliminar una key
del my_dict["edad"]
print(my_dict)
#y tambien la puedo añadir
my_dict["edad"]= 38
print(my_dict)
# y tambien se puede hacer un pop que es mejor que hacer del
edad=my_dict.pop("edad")
print(my_dict)
print(edad)
print("nombre" in my_dict)# da true
print("Sara" in my_dict)#da false porque busca por keys
#el fromkeys sirve para crear un diccionario con las mismas keys pero sin values
my_new_dic=my_dict.fromkeys("nombre", 0)
print(my_new_dic)