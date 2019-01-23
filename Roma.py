
#Escribe una función que tome como parámetros de entrada una cadena de caracteres (en mayúsculas) y una lista de enteros de
#  tamaño n** (n** la conseguiremos usando len() sobre la palabra introducida). Los enteros de la segunda lista deben
# ser menores o iguales que n**. La función devolverá al programa principal una matriz (nx**n) donde las letras del
#  primer vector estarán distribuidas como en el ejemplo.


def matriz(a,b):
    dev=[]
    for i in range(len(b)):
        dev.append([])
        for j in range(len(b)):
            if len(b)-int(b[j])<=i:
                dev[i].append(a[j])
            else:
                dev[i].append(' ')
    return dev

cadena = input('Escribe una palabra: ')
num =input('Escribe {} números entre i y {} separados por espacios: '.format(len(cadena),len(cadena))).split()
m = matriz(cadena,num)
for fila in m:
    for columna in fila:
        print(columna,end=' ')
    print()




