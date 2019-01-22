

M = int(input("Introduce el número de filas: "))
n = int(input("Introduce el número de columnas: "))


matriz = []
for i in range(M):
    Fila = [0]*n
    matriz.append(Fila)
    print(Fila)
print(matriz)



for i in range(M):
    for j in range(n):
        matriz[i][j] = int(input("Introduce un elemetno: "))

    print()
print(matriz)

