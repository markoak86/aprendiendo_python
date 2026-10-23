#1.crear una lista llamada mascotas, con 3 diccionarios, que contenga nombre, especie y edad de cada mascota
mascotas=[{"nombre": "quasi", "especie": "gato", "edad":10}, {"nombre": "piña", "especie": "gato", "edad": 9}, {"nombre": "pi", "especie": "cobaya", "edad": 3}]

#usa un bucle for para imprimir el nombre y la especie de cada mascota y un condicional que si tiene menos de 3 años ponga que es un cachorro
for animal in mascotas:
    nombre_mascota=animal["nombre"]
    especie_mascota=animal["especie"]
    edad_mascota=animal["edad"]
    print(nombre_mascota)
    print(especie_mascota)
    if edad_mascota<3:
        print("es un cachorro")

#2. MONITOR DE USUARIOS: crear una lista llamada usuarios, cada elemento es un diccionario que contiene nombre, ip y rol(admin o usuario)
usuarios= [{"nombre":"Luis Garcia", "ip": "192.168.0.1","rol":"usuario"},
{"nombre":"Sara Garcia", "ip": "192.168.0.4", "rol": "usario"},
{"nombre":"Luisa fernanda", "ip": "192.168.0.6", "rol": "usuario"},
{"nombre": "Marco Marco", "ip": "192.185.0.5", "rol": "admin"}]

for persona in usuarios:
    nombre_usuario= persona["nombre"]
    ip_usuario= persona["ip"]
    rol_usuario= persona["rol"]
    if rol_usuario=="admin":
        print(nombre_usuario, rol_usuario)

#3.LOGIN INFITO:crear un programa que pida contraseñas hasta que el usuario acierte
#crear una variable llamada password_correcta= "admin123"
password_correcta= "admin123"

#crear otra variable vacia llamada intento= ""
intento= ""

#usar un bucle que se ejecute mientras intento no sea admin123, si la contraseña es incorrecta poner "intento fallido"

while intento!=password_correcta:
    intento= input(str("introduzzca password:"))
    print("intento fallido,pruebe otra vez y pulse enter:")
    intento==password_correcta

print("bienvenido")

#4.BUSCADOR DE USUARIOS INTERACCTIVO:
#crear una lista con tres diccionario con nombre apellidos y rol
usuarios_nuevos=[{"nombre":"Marco", "apellido": "Marco", "rol": "administrador"}, 
                 {"nombre":"Luis", "apellido": "Garcia", "rol": "usuario"}, 
                 {"nombre":"Sara", "apellido": "Garcia", "rol": "usuario"}, 
                 {"nombre":"Patricia", "apellido": "Garcia", "rol": "administrador"},
                 {"nombre":"Jose Carlos", "apellido": "Jimenez", "rol": "usuario"},]

#usar un bucle para que el usuario escriba un nombre de usuario
busqueda=""
while busqueda!="salir":
    busqueda=input(str("introduzca un nombre o escriba salir y pulse enter:"))
    for persona in usuarios_nuevos:
        if busqueda==persona["nombre"]:
            print(persona)
busqueda=="salir"
print("saliendo del sistema")

    
    
       


    
 
    
    

       
   






      

    


      
 

    


    
   