

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
