
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


# Escribe un programa que lea una matriz de letras minúsculas m2 de rango 4x4. Una primera matriz m1 viene dada. El programa debe comparar los caracteres elemento a elemento y almacenar los caracteres que sean iguales en ambas matrices de la siguiente manera:
# -. En una lista d** si el carácter está entre la ‘a’ y la ‘m’ o
# -. en una lista **f si el carácter está entre la ‘n’ y la ‘z’.#



m1 = [['u', 'r', 'b', 'u'],
      ['o', 'a', 'e', 'i'],
      ['l', 'f', 'd', 'o'],
      ['o', 'r', 'c', 'i']]
print('La primera matriz es: ')
print()
for fila in m1:
    for elem in fila:
        print('{:2}'.format(elem),end='')
    print()
print()
m=[]
lista_d=[]
lista_f=[]
for i in range(4):
    fila=input()
    fila=fila.split()
    m.append(fila)
for i in range(4):
    for j in range(4):
        if m[i][j]==m1[i][j]:
            if m[i][j]>='a' and m[i][j]<='m':
                lista_d.append(m[i][j])
            elif m[i][j]=='ñ':
                lista_d.append(m[i][j])
            else:
                lista_f.append(m[i][j])
print('La lista d es:',' ',end='')
for i in lista_d:
    print(i,' ',end='')
print()
print('La lista f es:',' ',end='')
for i in lista_f:
    print(i,' ',end='')

