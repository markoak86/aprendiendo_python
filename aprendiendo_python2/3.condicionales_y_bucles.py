#CONDICIONALES: las estructuras condicionales funcionan por condiciones, si se cumple una condicion se ejecuta un bloque de codigo
#si no se comple se ejecuta el otro bloque de codigo, es jerarquico, primero se valora el if, despues elif y por ultimo el else.
numero=int(input("introduce un numero y pulsa enter:"))
if 6*4 < numero:
    print("el numero es mayor a 24")
elif 6*4 == numero:
    print("el numero es 24")
else:
    print("el numero es menor de 24")

#BUCLES:un bucle es un bloque de codigo que se ejecuta siempre y cuando se cumpla una condicion. Hay dos tipos:
#-WHILE: Se ejecuta el bloque de codigo siempre y cuando se cumpla una condicion
numero=20
while numero < 40:
    print(numero)
    if numero <= 30:
        numero=numero + 2
    else:
        numero= numero + 1 #se pueden meter condicionales dentro de bucles.

#-FOR IN: Es un bucle que itera sobre los elementos de una lista, tupla, set y diccionarios
lista=["Marco", 40, 1.90, "sysadmin"]
diccionario={"nombre": "Sara", "edad": 38, "altura":1.63, "trabajo":"optica"}
for elemento in lista:
    print(elemento)

for elemento in diccionario:#en los diccionarios itera por las llaves
    print(elemento)

for elemento in diccionario.values():#asi itera por los valores.
    print(elemento)

#TANTO PARA WHILE COMO PARA FOR IN, PARA SALIR DEL BUCLE SE USA LA PALABRA BREAK Y PARA SALTAR DE UNA ITERACION A LA SIGUIENTE SE UTILIZA LA PALABRA CONTINUE.