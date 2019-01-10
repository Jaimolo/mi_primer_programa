
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