archivo = open('prueba.txt', 'w')

archivo.write("Nuevo texto")
archivo.close()

archivo = open('prueba.txt')


print(archivo.read())

archivo.close()

archivo = open('prueba.txt', 'a')

archivo.writelines(["Federico\t", "20/12/2021\t", "08:17:32 hs\t", "Sin errores de carga"])
archivo.close()

archivo = open('prueba.txt')

print(archivo.read())
archivo.close()