#Diario Personal
from datetime import datetime

#Solicitar entrada del usuario 
entrada=input("Escribe tu entrada para el diario: ")

#Abrir el archivo en modo adicion "a"
with open("diario.txt", "a", encoding="utf-8") as archivo:
    fecha_hora_actual = datetime.now(). strftime("%Y-%m-%d %H:%M:%S")
    archivo.write(f"{fecha_hora_actual} - {entrada} \n")

print("Tu entrada ha sido guardada en el diario.")