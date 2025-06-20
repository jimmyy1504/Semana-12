#Abrir el archivo en modo lectura
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print("Lista de productos:\n")

    #Recorrer el archivo linea por linea
    for linea in archivo:
        #Eliminar el salto de linea final
        linea = linea.strip()

        #Separar los datos por coma
        partes = linea.split(",")
        if len(partes) == 3:
            nombre, precio, cantidad = partes
            
            #Imprimir de forma ordenada
            print(f"Producto: {nombre}   Precio: ${precio}    Stock: {cantidad} unidades")
        else:
            print("Linea con formato incorrecto: ", linea)
except FileNotFoundError:
    print("Error: El archivo 'productos.csv' no fue encontrado.")