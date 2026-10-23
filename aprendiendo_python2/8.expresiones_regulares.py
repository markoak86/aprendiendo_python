#EXPRESIONES REGULARES: son formas de buscar dentro de una cadena de texto.
#las expresiones regulares estan dentro del modulo re.
import re
mi_texto="Esta es la leccion numero 8, esta es la correspondiente a expresiones regulares."
mi_otro_texto="Esto no es la leccion 7, es la leccion la correspondiente con manejo de ficheros."

#MATCH:busca coincidencias, pero solo encuentra match si empieza desde el principio
print(re.match("Esta es la leccion", mi_texto))
print(re.match("Esta es la leccion", mi_otro_texto))
print(re.match("expresiones regulares", mi_texto))#no hace match porque empieza a buscar desde el principio

coincidencia=re.match("Esta es la leccion", mi_texto) #puede guardar el match
print(coincidencia)
print(coincidencia.span())#para acceder a los caracteres de inicion  y de cierre.

#SEARCH: es igual que match pero encuentra coincidencias empezando desde cualquier punto del string, pero solo encuentra la primera coincidencia.
print(re.search("Esta es la leccion", mi_texto))
print(re.search("expresiones regulares", mi_texto)) #encuentra la coincidencia entre el caracter 50 y 71
print(re.search("leccion", mi_otro_texto))#solo encuentra el primer leccion

#FINDALL: encuentra todas las coincidencias que haya en cualquier parte del string
encontrar_todo=re.findall("leccion", mi_texto)
print(encontrar_todo)
encontrar_todo_2=re.findall("leccion", mi_otro_texto)#encuentra los dos leccion que hay en el string
print(encontrar_todo_2)

#SPLIT:sirve para separar el string y lo convierte en una lista. separa los elementos por el elemento que nosotros le digamos.
mi_cadena_split=re.split(":", mi_texto)
print(mi_cadena_split)

#SUB: sirve para sustituir un elemento del string por otro
mi_otro_texto_mayuscula=re.sub("leccion", "LECCION", mi_otro_texto)
print(mi_otro_texto_mayuscula)

#I:es sensitive case
print(re.match("ESTA", mi_texto, re.I))

#PATRONES:los patrones se le pasan a un string para que encuentre dicho patron. se definen mas o menos como el formateo, pero con r"".
mi_patron=r"[Ee]sta"#esta con la e en mayuscula o en minuscula
#-despues le pasamos el patron a una cadena de texto
print(re.findall(mi_patron, mi_texto))#busca em mi_texto esta con la primera letra en mayuscula y en minuscula.

#ejemplo patron de validador de email con patrones
validador_email=r"^[a-zA-z0-9_+-]+@[a-zA-z0-9]+\.[a-zA-z0_9]+$"#^este caracter significa que empiece por, \ este siginifica que escape cualquier caracter menos el que va siguiente y $ sirve para indicar el final de la cadena
mi_email="markoak@hotmail.com"
#ahora vemos si la expresion regular machea con el email.
print(re.match(validador_email, mi_email))
mi_email_erroneo="markomarko.com"
print(re.match(validador_email, mi_email_erroneo))# este mail no retorna porque no tiene el arroba