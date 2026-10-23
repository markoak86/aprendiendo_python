#vamos a repasar las excepciones(try/except), y el datetime
import datetime
from datetime import datetime
fecha_de_auditoria=datetime(2026, 6, 20)


try:
    today=int(input("introduzca el dia de hoy(numero de dia del mes) y pulse enter:"))

    print(today)
except ValueError:
    print("ERROR: INTRUCE UN NUMERO")

now=datetime.now()
print(now)

diferencia=fecha_de_auditoria-now
print(f"faltan {diferencia.days} para la auditoria.")

#vamos a repasar las list comprehesion
servidores=["Srv-Web", "Srv-DB", "PC-Usuario","Srv-Backup","PC-Admin"]

#crear lista que solo contenga los servidores
solo_servidores=[i.lower() for i in servidores if i.startswith("Srv")]
print(solo_servidores)

ip_sucias=["192.168.1.10"," 10.0.0.5","192.168.1.20"," 8.8.8.8"]
ip_limpias=[i.strip() for i in ip_sucias if not i.strip().startswith("10")]
print(ip_sucias)
print(ip_limpias)
    