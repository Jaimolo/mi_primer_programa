

Matriz = []
N = int(input("Introduce el rango de la matriz cuadrada: "))

for i in range(N):
    filas = [0] * N
    Matriz.append(filas)
    print(filas)
print(Matriz)

for i in range(N):
    for j in range(N):
        Matriz[i][j] = int(input("Introduce el elemento en la posición {},{}: ".format(i,j)))

for i in range(N):
    print(Matriz[i])



