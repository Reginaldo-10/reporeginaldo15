archivo = "C:\\Users\\oeschle\\OneDrive\\lab5python\\documento.txt"
print(archivo)
with open(archivo) as archivo:
    for linea in archivo:
        print(linea.upper())

