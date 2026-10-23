#MANEJO DE PAQUETES: Para el manejo de paquetes hay que usar el PIP (gestor de paquetes de python), sirve para poder instalar, actualizar paquetes,etc a python

#-1. lo primero hay que instalar pip desde la consola(terminal) poniendo "py - m pip install"
#despues lo actualizamos para que tengamos la ultima version cn "py -m  pip install --upgrade pip"

#import numpy nos da error porque no tenemos le paquete instalado de numpy
#para poder importar el modulo primero hay que instalarlo con "py -m pip install numpy" en la terminal
import numpy # ya he podido importar el modulo numpy, numpy sirve para hacer operaciones complejas con numeros.
lista=[6,7,9,24]
lista_por_dos=lista*2
print(lista_por_dos)#dupilica la lista
array=numpy.array(lista) #transformamos la lista en array (un array es una lista, pero todos sus elementos son del mismo tipo de datos) para poder operar con ellos
array_por_dos=array*2
print(array_por_dos)#multiplica por dos cada el elemento del array

#en la terminal el comando py -m pip list sirve para ver todas las librerias que tenemos instaladas
#en la terminal, para desinstalar paquetes pues hay que usar en la terminal el comando "py -m pip uninstall numpy"
# al haber desinstalado numpy ya no puedo importar el modulo. asique vuelvo a instalarlo.
