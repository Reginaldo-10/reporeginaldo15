# Ruta del archivo
archivo = "C:\\Users\\oeschle\\OneDrive\\lab5python\\documento.txt"
print(archivo)          # Imprimir el nombre del archivo

with open(archivo, 'r', encoding='utf-8') as f:
    for linea in f:
        print(linea.upper())