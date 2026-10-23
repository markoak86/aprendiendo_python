#se te proporciona una cadena de texto con este formato nombre: Juan, edad: 30, ciudad: Madrid
cadena= "nombre:Juan, edad:30, ciudad: Madrid"
#esta cadena de texto tiene estructura de diccionario, asique la transformamos en diccionario
my_dict= {}
for par in cadena.split(","):
    clave, valor= par.split(":")
    my_dict[clave.strip()]=valor.strip()
print(my_dict)
print(type(my_dict))

#extrae la edad de la persona y dividela por 2
#en estos momentos edad es un estrig asique hay que pasarlo a int
my_dict["edad"]=int(30)
print(my_dict["edad"])
print(type(my_dict["edad"]))
#ahora la dividimos entre dos
my_dict["edad"]=my_dict["edad"]/2
print(my_dict)

#extraer la ciudad y reemplazarla por Barcelona
my_dict["ciudad"]="Barcelona"

#construir una nueva cadena de texto con la nueva ciudad
print(my_dict)
nueva_cadena= str(my_dict)
print(nueva_cadena)
print(type(nueva_cadena))







