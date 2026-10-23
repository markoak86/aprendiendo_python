#CONDICIONALES: los condicionales if significa que mientras se cumple la condicion se ejecuta el codigo
#por eso primero hay que definir primero una condición
my_condiccion1= 8*4
my_condiccion2= 8+4
if my_condiccion1 <12:
    print("mi condicion se cumple por que el numero es 32")
elif my_condiccion2 ==6*3:
    print("el numero es 12")
else:#si no se cumple la condicion entonces se ejecuta lo siguiente
    print("mi condicion no se cumple porque la condicion 1 no es menor de 12(es 32), ni la condicion 2 es 18(es 12)")
    #tiene como un nivel jerarquico, primero: se cumple el if, si no, se cumple elif y si tampoco, pues ejecuta el else


#BUCLES(LOOPS):significa que se repite un codigo mientras se cumple una condicion, tipos:

#WHILE es como un if pero que se repite el codigo mientras se cumple una condicion
numero= 32#punto de inicio del bucle
print(numero)
while numero <=48:
    print("se ejecuta")
    print(numero)
    numero +=2
    if numero== 40:
        break
#se pueden meter condicionales dentro de un while y si queremos que el bucle se detenga antes podemos meter break

#FOR_IN: es como while pero para listas,tuplas, sets y diccionarios, va buscando elemento por elemento
#FOR es un bucle determinado por que el programa sabe cuantas veces tiene que repetir el codigo, normalmente se hace con listas,tuplas,diccionarios,sets, pero tambien se puede hacer con un string
my_list=["casa", 40.8, 30, "palito"]
my_dict= {"nombre": "marco", "edad": 39, "altura": 1.89}
for element in my_list:
    print(element)

for element in my_dict:
    print(element)#imprime keys

for element in my_dict.values():
    print(element)#imprime valores

for element in my_list:
    print(element)
    if element==30:
        break
    
#ejemplo validacion de email;se valida cualquier email que contenga una arroba
email=input("introduce la direccion de email a validar:")
control=False
for letra in email:
    if letra == "@":
        control=True

if control==True:
    print("la direccion es correcta")
else:
    print("la direccion es falsa")

#ahora el email tiene que tener solo una arroba y al menos un punto
email=input("introduce la direccion de email a validar:")
control_arroba=0
control_punto=False
for letra in email:
    if letra==".":
        control_punto=True

    if letra=="@":
        control_arroba=control_arroba+1

if control_punto==True and control_arroba==1:
    print("el correo es bueno")
else:
    print("el correo es malo")