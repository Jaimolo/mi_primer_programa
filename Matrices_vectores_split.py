
#Escribe un programa que almacene números en dos listas a** y **b de tamaño N** (N** constante conocida) y devuelva otra lista c** que contenga
#  la multiplicación de **a y b** elemento a elemento. Diseñaremos una función llamada **lee_lista que usaremos para leer el vector a** y el vector
#  **b en dos llamadas sucesivas. También crearemos una función llamada construye para obtener c** a partir de **a y b** y finalmente diseñaremos
# otra función **escribe_lista que muestre por pantalla a*, *b y c** en tres llamadas sucesivas.#

def lee_lista(p):
    p = p.split()
    for i in range(len(p)):
        p[i] = int(p[i])
    return p


def construye(a, b):
    s = []
    for j in range(len(a)):
        s.append(a[j] * b[j])
    return s


def escribe_lista(z):
    for i in z:
        print(i, ' ', end='')
    print()


lista_1 = input('Escribe 6 números separados por espacios: ')
lista_2 = input('Escribe otros 6 números: ')
a = lee_lista(lista_1)
b = lee_lista(lista_2)
c = construye(a, b)
print('La lista a es: ', end='')
escribe_lista(a)
print('La lista b es: ', end='')
escribe_lista(b)
print('La lista c es: ', end='')
escribe_lista(c)