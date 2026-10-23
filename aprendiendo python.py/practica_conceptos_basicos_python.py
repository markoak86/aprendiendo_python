#GESTOR DE ACCESOS A UNA RED:
#1.crear una clase llamada usuario
class Usuario:
    def __init__(self, nonmbre_de_usuario, rol):
        self.nombre_de_usuario=nonmbre_de_usuario
        self.rol=rol
        self.servicios=[]
#2.crear un diccionario y una lista para servicios
base_datos_usuarios={}
servicios=[]
#3.crear el bucle para que imprima el menu
while True:
    try:
        print("MENU")
        print("1.registrar usuario")
        print("2.asignar servicios")
        print("3.listar accesos")
        print("4.salir")
    
        opcion=int(input("introduzca un numero y pulsa enter:"))
    except ValueError:
        print("introduce un numero correcto")
    
    

    #crear los condicionales para las distintas opciones
    if opcion==4:#la opcion 4 sale del bucle
        print("SALIENDO DEL SISTEMA")
        break
    elif opcion==1:#la opcion 1 crea el objeto dentro de la clase
        nombre_de_usuario=str(input("introduzca su nombre de usuario y pulse enter:"))
        rol=str(input("introduzca su rol y pulse enter:"))
        
        print(f"el usuario {nombre_de_usuario} se ha guardado con exito")

        nuevo_usuario= Usuario(nombre_de_usuario, rol)#se crea el objeto dentro de la clase

        base_datos_usuarios[nombre_de_usuario]=nuevo_usuario#se guarda el objeto nuevo usuario en el diccionario
    elif opcion==2:#la opcion 2 añade los servicios a la lista servicios con el .append
        nombre_de_usuario=str(input("introduzca su nombre de usuario y pulse enter:"))
        if nombre_de_usuario in base_datos_usuarios:
            nuevo_servicio= str(input("introduce el nombre del servicio y pulsa enter:"))
            base_datos_usuarios[nombre_de_usuario].servicios.append(nuevo_servicio)
            print("nuevo servicio añadido")
        else:
            print("usuario no encontrado")
    elif opcion==3:#con la opcion 3 creamos un bucle for in para que recorra todos los elentos del diccionario
        if not base_datos_usuarios:
            print("la base de datos esta vacia")
        else:
            for b in base_datos_usuarios.values():
                print(f"NOMBRE DE USUARIO: {b.nombre_de_usuario}")
                print(f"ROL: {b.rol}")
                print(f"SERVICIOS: {b.servicios}")
            input("pulse enter para volver al menu")
