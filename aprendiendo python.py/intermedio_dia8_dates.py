#DATES: fechas y operaciones con ellas
#primero hay que importar el module datetime
import datetime
#dentro de datatime existe datetime que sirve para fecha y hora, y puedes acceder a la fecha y hora actual con now o poner la quieras
#se puede hacer de dos formas
#primera
now=datetime.datetime.now()
print(now)
#segunda
from datetime import datetime
hoy=datetime(2028,3,4)
print(hoy)#tambien podemos definir nosotros la fecha que queramos

now=datetime.now()#o la fecha de hoy

print(now)



year= now.year#asi dividimos la fecha en partes

mounth= now.month
day=now.day
hour=now.hour
minut=now.minute
second=now.second
time_stamp=now.timestamp
print(time_stamp())#el time estamp es una forma de plasmar la fecha que la entienden las computadoras de forma internacional, independientemente de la zona horaria


def date_complete():
    print(year)
    print(mounth)
    print(day)
    print(hour)
    print(minut)
    print(second)

print(date_complete())
print(date_complete())

nueva_fecha=hoy-now#tambien se puede operar con fechas y horas sumando o restando
print(nueva_fecha)
#las operaciones solo se pueden hacer con datos del mismo modulo(datetime,date o time)

#dentro del modulo datetime esta date, que sirve para establecer solo fechas,sirve tanto para acceder a la fecha de hoy con today o para poner la fecha que queramos
from datetime import date
fecha=date(2027,3,4)
print(fecha)
fecha_hoy=date.today()
print(fecha_hoy)#o poner la fecha de hoy


#dentro de datetime tambien esta time, que sirve para poner la hora que queramos pero no para acceder a la hora actual
from datetime import time
hora=time(12,40,13)
print(hora)

#dentro de datetime tambien esta timedelta que sirve para trabajar con periodos de tiempo, no con fechas concretas
from datetime import timedelta
periodo1=timedelta(weeks=23,days=49)
periodo2=timedelta(weeks=59,days=97)
print(periodo1)
print(periodo2)
nuevo_periodo1=periodo2+periodo1
print(nuevo_periodo1)
nuevo_periodo2=periodo2-periodo1
print(nuevo_periodo2)

