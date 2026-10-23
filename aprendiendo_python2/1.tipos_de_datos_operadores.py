#LOS TIPOS DE DATOS EN PYTHON SON STRINGS, ENTEROS, FLOTANTES Y BOOLEANOS
print("esto es una cadena de caracteres porque va entre comillas")
print("esto es un entero", 5)
print("esto es un numero flotante porque va como un punto", 5.4)
print("los booleans son:", True, False)
#convertir entre tipos de datos
numero=5
print(type(numero))
numero_convertido_string=str(numero)
print(type(numero_convertido_string))

#FORMATEAR STRINGS
name= "Marco"
age= 40
print(f"mi nombre es {name} y mi edad son {age} años")
#salto de linea y tabulacion con strings
print("mi nombre es Marco\ntengo 40 años")
print("mi nombre es MARCO\ttengo 40 años")
#metodos para formatear strings
frase="esta es una frase"
print(frase.capitalize())#primer caracter lo combierte en mayuscula
print(frase.upper())# todo en mayusculas
print(frase[4])#extrae el cuarto caracter, hay que tener en cuenta que empieza por 0
print(frase[:4])#extrae los caracteres anteriores, pero sin contar el 4
print(frase[4:])#extrae los caracteres posteriores, contando con el 4

#VARIABLES EN PYTHON: Las variables son espacios de memoria a los que se les asigna un valor o un dato y que pueden variar con el tiempo.
nombre="Sara"
edad=38
estatura=1.53
print(nombre, edad, estatura)
nombre="Marco"
print(nombre, edad, estatura)
print(type(nombre))#para ver el tipo de dato de la variable
print(type(edad))
print(type(estatura))
suma=4+7
print(suma)
print(type(suma))
suma_string=str(4+7)
print(suma_string)
print(type(suma_string))

#OPERADORES EN PYTHON: ARITMETICOS, DE COMPARACION Y BOOLEANOS.
#operadores aritmeticos
print(4+6)
print(4*6)
print(6/4)
print(6%4)#modulo o resto
print(6//4)#division redondeada
print(6**4)#potencia
#operadores de comparacion
print(6<4)
print(6>4)
print(6<=4)
print(6>=4)
print(6==4)
print(6!=4)
print("hola"<"quesadilla")#comaparacion por orden alfabetico
print(len("hola")<len("quesadilla"))#comparacion por lengitud
#operadores booleanos
print((6>4) and (7>4))#and es true siempre que ambas condiciones sean true, si no, es false
print((7>4) or (4<8))#or es true siempre que una de las condiciones true, si no, es false
print(not(6>4))#not cambia el signo de la condicion, si es false lo cambia a true y vicebersa
#is, is not
a=5
b=6
print(a is b)
c=7
d=7
print(c is d)
#in, not in
lista=[4,5,3,6,8]
print(6 in lista)
print(6 not in lista)