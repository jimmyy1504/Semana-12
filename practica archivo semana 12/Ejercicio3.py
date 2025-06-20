#Generador de listas de compras
with open("compras.txt", "w", encoding="utf-8") as archivo:
    print("Generador de listas de compras")
    print("Escribe los productos uno por uno. Escribe 'fin' para terminar.\n")

    #Crear un ciclo
    while True:
        producto=input("Ingresa un producto: ")
        if producto.lower() == "fin":
            break
        archivo.write(producto + "\n")
print("Lista de compras guardada en 'compras.txt'.")