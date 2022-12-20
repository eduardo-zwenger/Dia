mi_archivo = open('Dia 6.txt')

print(mi_archivo.readline())


mi_archivo.close()


mi_archivo = open('Dia 6.txt')

print(mi_archivo.read())

mi_archivo = open('Dia 6.txt')

segunda_linea = mi_archivo.readlines().pop(1)


print(segunda_linea)
