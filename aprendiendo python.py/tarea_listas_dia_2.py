#crear lista con los elementos (a,c,d,a,l,m)
lista=["a", "c", "d", "a", "l", "m"]
print(lista)
print(type(lista))
#usa un metodo para saber el numero de veces que aparece el caracter a en la lista
print(lista.count("a"))
#utiliza un metodo para elimininar el caracter d de la lista
lista.remove("d")
print(lista)
#añadir en la posicion 2 de la lista el caracter p
lista.insert(2, "p")
print(lista)
#utilizar un metodo para ordenar la lista alfabeticamente
lista.sort()
print(lista)