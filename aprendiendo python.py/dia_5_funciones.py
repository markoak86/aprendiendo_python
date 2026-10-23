#FUNCIONES:las funciones son porciones de codigo que sirven para no repetir codigo en un programa ahorrando tiempo y minimizando errores
#lo primero, las funciones hay que definirlas con la palabra clave def
def my_funtion():#esto es una funcion sin argumentos
    print("esta es my funcion sin argumentos")
#una vez hayamos definido la funcion la podemos llamar cuando queramos
print(my_funtion())

#tambien las funciones pueden tener argumentos
def my_name_with_two_surname(name,surname1,surname2):
    
    print(f"mi nombre es {name}, mi apellido es {surname1} y my segundo apellido es {surname2}")
print(my_name_with_two_surname("marco", "marco","quiros"))

#podemos tambien poner argumentos por defecto
def sara(name,surname,ocupation="optica"):
    print(f"mi nombre es {name}, mi apellido es {surname} y mi trabajo es {ocupation}")

print(sara("Sara","Quiros","responsable de mercado"))
print(sara("Sara","Quiros"))



#tambien se pueden cambiar los argumentos
print(sara(surname="quiros",name="sara"))

#podemos crear funciones con retorno de parametros, esos parametros retornados se guardan en una variable
def sum_num(num1,num2):
    return(num1+num2)
resul=sum_num(8,65)
print(resul)

#tambien podemos crear funciones que acepten un numero variable de argumentos con el simbolo *
def sumar(*numeros):
    sumar=sum(numeros)
    print(sumar)
    

print(sumar(5,6,7))
    