
# Crea un programa que reciba tres vectores y cree un vector D formado por la media de cada uno de los anteriores#

def leelista(nombre):
    print("Introduce los elementos del vector",nombre,": ")
    v = input()
    v = v.split()
    for i in range(len(v)):
        v[i] = int(int(v[i]))
    return v

def calcula(v):
    media = sum(v)/len(v)
    dif = max(v)-min(v)
    for elem in v:
        if abs(media - elem)<= dif:
            dif = abs(media - elem)
            cerca = elem
    return cerca

a = leelista('A')
b = leelista('B')
c = leelista('C')
d = []

d.append(calcula(a))
d.append(calcula(b))
d.append(calcula(c))

print("Vector D: ",d)

#Esctibe un programa que te permita introducir una matriz y te diga si es simétrica#

N=3
print('Introduce una matriz de {}x{} elementos:'.format(N,N))
print()
m=[]
n=[]
simetria=False
for i in range(N):
    fila=input()
    fila=fila.split()
    for i in range(N):
        fila[i]=int(fila[i])
    m.append(fila)
for i in range(N):
    for j in range(N):
        if m[i][j]==m[j][i]:
            simetria=True
if simetria:
    print('La matriz es simétrica')
else:
    print('La matriz no es simétrica')