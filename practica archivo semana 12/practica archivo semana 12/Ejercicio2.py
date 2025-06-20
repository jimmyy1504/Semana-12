#Contador de lineas

#Solicitar el nombre del archivo
nombre_archivo = input("Ingresa el nombre del archivo: ")
#Abrir el archivo en modo lectura
try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

        #Contar y mostrar la cantidad de lineas 
        cantidad_lineas = len(lineas)
        print(f"El archivo tiene {cantidad_lineas} linea(s).")
except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado. ")