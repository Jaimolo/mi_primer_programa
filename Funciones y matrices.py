

def lee_matriz(nombre, dim):
    print("Vamos a meter la matriz",nombre,"de dimensión" ,dim,"x",dim,": ")
    print()
    m = []
    for i in range(dim):
        fila = [0] * dim
        m.append(fila)
    for i in range(dim):
        for j in range(dim):
            m[i][j] = int(input("Mete un elemento {},{}: ".format(i, j)))
    print()
    return m


m1 = lee_matriz('M1',3)
m2 = lee_matriz("M2",4)
m3 = lee_matriz("M3",2)

print(m1)
print(m2)
print(m3)