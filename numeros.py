# Abre un archivo en modo escritura
with open('numeros.txt', 'w') as archivo:
    # Escribe los números del 1 al 100,000 en el archivo
    for numero in range(1, 100001):
        archivo.write(str(numero) + '\n')
