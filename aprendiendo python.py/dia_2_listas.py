#list: las listas se definen entre corchetes y los elementos se separan por comas o formalmente
lista= list()
my_list=["marco", 39, 1.90, "casado", "sara", 38, 1.60, "casado"]
print(my_list)
print(type(my_list))
#len te da el numero de elementos que tiene la lista
print(len(my_list))
#count te da el numero de veces que aparece un elementos
print(my_list.count(39))
print(my_list.count("casado"))
#tambien se pueden sumar listas
my_new_list=[49, 58, 69, "paleto", "galleta", -54]
print(my_list+my_new_list)
#se puede tambier ver un elemento de la lista por el numero de indice
print(my_list.index("casado"))#te dice el numero de indice de un elemento
print(my_new_list[4])
print(my_new_list[-1])#tambien se puede ver desde el ultimo elemento
#para añadir elementos:
my_list.append("chascarrillo")#se añade por el final
print(my_list)
my_list.insert(2, 24)#se añade por indice y se corren todos los siguientes elementos una posicion
print(my_list)
#tambien se pueden sustituir elementos en una lista
my_list[1]="caminito"
print(my_list)
#para eliminar elementos de una lista
print(my_list)
my_list.remove("casado")#elimina el primer elemento que encuentra
print(my_list)
my_list.pop(0)#para desapilar un elemento de una lista
print(my_list)
name= my_list.pop(0)#para desaapilar un elemento de una lista y guardarlo en una variable
print(name)
print(my_list)
del my_list[3]# para eliminar elementos por indice
print(my_list)
my_list.clear()#elimina toda la lista pero la lista sigue existiendo
print(my_list)
#copiar listas en otra lista
my_list=my_new_list.copy()
print(my_list)
print(my_new_list)
my_list.append("perrito")
print(my_list)
print(my_new_list)
#ordenar listas
my_list.reverse()#invertir elementos
print(my_list)
ages=[83, 45, 98, 6, 3, 34, 95]
print(ages)
ages.sort()#ordenar de mayor a menor
print(ages)