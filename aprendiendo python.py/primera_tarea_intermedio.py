#GESTION DE STOCK INTELIGENTE:
#crear una lista con varios diccionarios:
inventario= [{"nombre":"laptop","precio":1200, "cantidad":5, "categoria":"computo"},
            {"nombre":"mouse","precio":25, "cantidad":50, "categoria":"accesorios"},
            {"nombre":"teclado","precio":80, "cantidad":12, "categoria":"accesorios"},
            {"nombre":"monitor","precio":300, "cantidad":0, "categoria":"computo"},
            {"nombre":"usb-c","precio":45, "cantidad":20, "categoria":"accesorios"}]
print(inventario)

#hacer una list comprehesion para filtrar los producctos de los que no halla stock
producctos_disponibles=[i for i in inventario if i["cantidad"]>0]
print(producctos_disponibles)

#crear un loop para recorrer cada producto y clacular la cantidad total del inventario
resumen_de_stock=0
valor_total=0
for producto in inventario:
    nombre=producto["nombre"]
    precio=producto["precio"]
    cantidad=producto["cantidad"]
    categoria=producto["categoria"]
    cantidad_total+=producto["cantidad"]
resumen_de_stock=cantidad_total
valor_total=precio*cantidad

print(resumen_de_stock)
print(valor_total)
print(resumen_de_stock)




