#LIST COHOMPRESION:las listas comprimidas es una forma de crear listas,pero sobre nos permite operar con listas a la vez que la creamos
my_list=[1,2,3,4,5,6,7,8]
print(my_list)

my_other_list=list(range(9))
print(my_other_list)

#creacion de listas con list cohompresion
my_new_list=[i for i in range(10)]
print(my_new_list)

#creacion de listas a la par que operamos con ellas

sum_list=[i+2 for i in range(20)]
print(sum_list)

multi_list=[i*3 for i in sum_list]
print(multi_list)

#incluso podemos pasarle funciones
def sum_five(numero):
    return(numero+5)

sum_five_list=[sum_five(i) for i in sum_list]
print(sum_five_list)