def abrir_leer(archivo):
    archivo = open('prueba.txt')
    return archivo.read()

def sobrescribir(archivo):
    archivo = open(archivo, 'w')
    return archivo.write(
"contenido eliminado")


def registro_error(archivo):
    archivo = open(archivo, 'a')
    return archivo.write("se ha registrado un error de ejecución")
    archivo.close()



