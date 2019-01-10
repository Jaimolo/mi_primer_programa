

#Como imprimir una matriz#

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for fila in m:
    for elemento in fila:
        print('{:5}'.format(elemento), end='')
    print()


# Como crear una matriz#

f = int(input("Introduce el número de filas de tu matriz: "))
c = int(input("Introduce el número de columnas de tu matriz: "))

matriz = []

for i in range(f):
    m.append([0]* c)
for i in range(f):
    for j in range(c):
        m[i][j] = int(input('Elemento {}, {}: '.format(i, j)))



# Esctibe un programa que pida un número y nos de su tabla de multiplicar#

def tabla(num):
    t = []
    for i in range(11):
        t.append(num * i)
    return t


n = int(input("Mete un número: "))
tb = tabla(n)
print(tb)




