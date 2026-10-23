#tipos de datos en python: string, enteros, float, booleanos y complejos.
print("esto en una cadena de caracteres porque va entre comillas")
print("esto es un numero entero", 5)
print("esto es un numero float", 5.9)
print("esto es un booleano", True, False)

#las variables en python son de tipado dinamico, esto quiere decir que se pueden cambiar el tipo de dato a lo largo de la ejecución del programa.
variable_string="hola mundo"
print(variable_string)
print(type(variable_string))
variable_string=5
print(variable_string)
print(type(variable_string))
suma=5+3
print(suma)
suma_string=str(suma)
print(suma_string)
print(type(suma_string))
print(len(suma_string))#len solo muestra longitud de datos string

#operadores en python: aritmeticos, comparativos, booleanos.
#operadores aritmeticos
print(5+2)
print(5-2)
print(5*2)
print(5%2)#modulo o resto de la division
print(5/2)
print(5**2)#exponente, 5 elevado a 2
print(5//3)#dividir y aproximacion
print("hola"+"hola")
print("hola"*3)
#operadores de comparación
print(5<3)
print(5>3)
print(5<=3)
print(5>=3)
print(5==3)
print(5!=3)
print("hola"<"castaña")#comparacion por orden alfabetico
print(len("casa")<len("cesto"))#comparacion por longitud
#operadores booleanos and or not
print((5>3)and(8>3))# los 2 true para que de true, si hay un false entonces false
print((4<2)or(4>2))#si hay un true o dos da true, solo si los dos son false da false
print(not(5>3))#cambia el signo, si es true da false y a la inversa

#string
print("hola\nmundo")#\n salto de linea en un string
print("hola\tmundo")#\t tabulacion en un strings
mi_str="python"
print(mi_str[3])#extraer posicion
print(mi_str[:2])#extraer anterior a
print(mi_str[2:])#extraer apartir de
print(mi_str.capitalize())
print(mi_str.isnumeric())
print(mi_str.count("t"))
print(mi_str.upper())
#formatear de dos formas distintas string, la mejor es la segunda
name="Marco"
age=35
texto="me llamo %s y mi edad es %d" % (name,age)
print(texto)
texto=f"me llamo {name} y tengo {age} años"
print(texto)

#is y is not sirven para comparar si dos objetos tienen la misma referencia de memoria
a=5#los enteros pequeños comparten la misma referencia en memoria por optimizacion
b=5
print(a is b)
l1=[1,2,3,4]#las listas no comparten la misma referencia de memoria, por lo que aunque tengan el mismo contenido, son objetos diferntes
l2= [1,2,3,4]
print(l1 is l2)

#in y not in sirve para ver si un elemento esta dentro de un objeto
print(2 in l1)
print(7 in l1)

l3=[1,2,3]
l4=[4,5,6]
print(l3)
l3=l4#hemos cambiado el valor de l3 por el de l4
print(l3)




