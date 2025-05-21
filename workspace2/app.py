import numpy as np 


#arreglo de una dimension
a=np.array([1,2,3,4,5])

#shape significa formato
print(a.shape)
print('Element extracted of index 2: ', a[2])

#arreglo de dos dimensiones
b=np.array([[1,2,3],[11,22,33]])
print(b.shape)
print('Extracted element of row 1 and column 2:', b[1,2])

print(b)

print ("OK :)")

c=np.zeros((5,4))
print("The matrix x is: ")
print(c)


d=np.ones((3,4))
print("Matrix of values ones: ")
print(d)

e=np.full((3,4),8)
print("Matrix of a unique values")np.rand


f=np.random.randint(1,11,size=(5,5))
print(f)

print("___________________________________")


print("Matrix G")
g=np.random.random((5,5))
print(g)

print("___________________________________")

print("Identifique matrix ")
h=np.eye(10)
print(h)


print("___________________________________")

print("SUBMATRIX")
f=np.random.randint(1,21,size=(3,4))
print(f)

m=f[:2,2:]
print(m)

print("___________________________________")

n=np.random.randint(1,101,size=(7,5))
print(n)
p=n[4:6,2:4]
print(p)


print("___________________________________")

o=n[2:5, 1:4]
print(o)


print("___________________________________")
k = n[[0, 0, -1, -1], [0, -1, 0, -1]]
print(k)

print("___________________________________")
# 0.0
# 6.0
# 6.4
# 0.4

h=n[[0,6,6,0],[0,0,4,4]]
print(h)
print(type)
print(h.shape)
print(h.ndim)


print("___________________________________")
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(p)
b=np.array([0,2,0,1])
a=np.arange(4)
#print(a)

print("___________________________________")
print(np.arange(4),b)
p[a,b]+=100
print(p)

print("___________________________________")
# Arrays de índices
b = np.array([0, 1, 2])  # Columnas de los elementos a modificar
a = np.array([0, 1, 2])  # Filas de los elementos a modificar

print("----")
print(np.arange(4), b)

# Alterar los valores 1, 5, 9 (en posiciones 0,0; 1,1; 2,2) sumando 200
p[a, b] += 200

print("Matriz después de agregar 200 a 1, 5 y 9:")
print(p)

filter=(p>5)
print(filter)
print (type(filter))
print(filter.ndim)
print(filter.shape)
z=p[filter]
print(type(z))
print(z.shape)
print(z.ndim)

print(z)

print("___________________________________")

filter=(p>5)
print(filter)
print(type(filter))
print(filter.ndim)
print(filter.shape)
z=p[filter]
print(type(z))
print(z.ndim)
print(z.shape)

print(z)

print("___________________________________")
print("Matriz con valores entre 40 y 60 reemplazados por 0:")

f = np.random.randint(1, 101, size=(7,7))  
print(f)

print("__________")

# filtro booleano
filter1=(f>40)
filter2=(f<60)
print('Filter 1')
print(filter1)
print('Filter 2')
print(filter2)
# funcion logica and &
print("____")
f[filter1 & filter2]=0
print(f)
print(f.shape)
print(type(f))

print("______________________________")
print("Matriz con múltiplos de 10 reemplazados por 200:")

# Generar la matriz
f = np.random.randint(1, 101, size=(7,7))  
print("Matriz original:")
print(f)

print("__________")

# Filtro para múltiplos de 10, reemplaza residuos
filtro3= (f % 10 == 0)
print("Filtro de múltiplos de 10:")
print(filtro3)

# Reemplazar múltiplos de 10 por 200
f[filtro3] = 200

print("Matriz modificada pares :")
print(f)
print(f.shape)
print(type(f))

print("______________________________")

# Filtro para números impares
#!=: "distinto de". Compara si algo no es igual a otro valor.
filtro4 = (f % 2 != 0)
print("Filtro de impares:")
print(filtro4)

# Elevar al cuadrado los impares
f[filtro4] = f[filtro4] ** 2

print("Matriz modificada impares:")
print(f)
print(f.shape)
print(type(f))

print("______________________________")

a = np.random.randint(1, 10, size=(2,2))  
b = np.random.randint(1, 10, size=(2,2))  
print("Matrix A")
print(a)
print("Matrix B")
print(b)

print("Adding matrices")
adding_matrices=np.add(a,b)
print(adding_matrices)

print("______________________")
print("Operaciones 1 forma")
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("______________________")
print("Operaciones 2da forma")
aux1=np.subtract(a,b)
aux2=np.multiply(a,b)
aux3=np.divide(a,b)
aux4=np.sqrt(a)

print(aux3)

print("______________________________")

a = np.random.randint(1, 10, size=(3,3))  
b = np.random.randint(1, 10, size=(3,3))  
c=a.dot(b)
print(c)
print(c.shape)
print(c.ndim)

print("______________________________")

a = np.random.randint(1, 10, size=(6,6))  
b = np.random.randint(1, 10, size=(6,6))  
print("Matrix A")
print(a)
print("Matrix B")
print(b)
#La funcion np.dot(a, b) realiza el producto matricial entre dos matrices. 
#Es decir, multiplica la matriz a por la matriz b siguiendo las reglas del algebra lineal.
c= a.dot(a, b)
print("A · B :")
print(c)
# print(c.shape)
# print(c.ndim)



print("______________VECTORES________________")
a=np.random.randint([[1,2],[3,4]])  
b=np.random.randint([[5,6],[7,8]]) 
print(a)
print(b)

w=np.array([9,10])
v=np.array([11,12])

tmp1=np.dot(w,v)
tmp2=w.dot(v)


print(tmp1)
print(tmp2)
print(type(tmp1))
print(type(tmp2))
print(tmp2.shape)
print(tmp1.ndim)


print("DOT PRODUCT BETWEEN A VECTOR AND MATRIX")
tmp3=a.dot(v)
tmp4=np.dot(a,v)
print(type(tmp3))
print(tmp3.ndim)
print(tmp3.shape)


print("_____________MATRIZ CUADRADA_________________")

a=np.random.randint([[1,2],[3,4]])  
print(a)
# result=np.sum(a)
print("EL RESULTADO DE LA SUMA DE TODOS LOS ELEMENTOS DENTRO DE LA MATRIZ ES: ", np.sum(a))

print("_____________SUMA_________________")

f = np.random.randint(1, 21, size=(15,15)) 
print(f)

# Sumar las filas (axis=1) y las columnas (axis=0)
# sum_filas = np.sum(f, axis=1)
sum_columnas = np.sum(f, axis=0)


# axis=1 indica que queremos sumar por fila (horizontalmente).
# print("\nSUMA DE CADA FILA:")
# for i, suma in enumerate(suma_filas):
#     print(f"Fila {i+1}: {suma}")


# axis=0 indica que queremos sumar por columna (verticalmente).
print("SUMA DE CADA COLUMNA:")
for j, suma in enumerate(sum_columnas):
    print(f"Columna {j+1}: {suma}")

print("_____________SUMA_________________")

f = np.random.randint(1, 21, size=(15,15)) 
print(f)

print("______________________________")
print("COLUMNA")
print("______________________________")

columns_sum=np.sum(f,axis=0)
print("SUMA: ", columns_sum)
print(columns_sum.shape)
print("TOTAL: " ,len(columns_sum))
print(columns_sum.ndim)
print("PROMEDIO COLUMNAS: " ,np.sum(f,axis=0)/len(np.sum(f,axis=0)))

print("______________________________")
print("FILAS")
print("______________________________")

columns_sum=np.sum(f,axis=1)
print("SUMA: ", columns_sum)
print(columns_sum.shape)
print("TOTAL: " ,len(columns_sum))
print(columns_sum.ndim)

prom = np.mean(f, axis=1)
print("PROMEDIO POR FILAS:")
print("PROMEDIOS: ", prom)
# print("THE AVEGARE OF EACH COLUMN ARE: ", np.average(f,axis=0))



print("________________________________________")
print("TRANSPOSE MATRIX ")
print("________________________________________")



print("_________________")
print("CUADRADA ")
print("_________________")
f = np.random.randint(1, 21, size=(4,4)) 
print(f)
print(f.T)

print("__________________")
print("NO CUADRADA ")
print("__________________")
f = np.random.randint(1, 21, size=(4,7)) 
print(f)
print(f.T)

print("__________________")

x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v=np.array([1,0,1])
emptyMatrix=np.empty_like(x)

print(x)
print(v)
print(x.shape)
print('rows: ', x.shape[0])
# print('columns', x.shape[1])
# for i in  range(x.shape[1]):
print("I")
for i in range(x.shape[0]):
    emptyMatrix[i,:]=x[i,:]+v
    # print(i)
print(emptyMatrix)


print("NP")
vv=np.tile(v,(4,1))
print(vv)
print(x+vv)

print("MANERA DIRECTA")
print(x+v)

print("______________hstack y vstack______________")
#hstack (horizontal stack) y vstack (vertical stack)
x=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

# Vector columna (4 filas, 1 columna)
v_col = np.array([[100], [200], [300], [400]])
# Vector fila (1 fila, 3 columnas)
v_row = np.array([[10, 20, 30]])

result_hstack = np.hstack((x, v_col))
print("Resultado de hstack:")
print(result_hstack)

result_vstack = np.vstack((x, v_row))
print("Resultado de vstack:")
print(result_vstack)

# | Operacion     | Que hace?            | Condicion                  | Resultado    |
# | ------------- | --------------------- | -------------------------- | ------------ |
# | `np.hstack()` | Agrega **columna(s)** | Misma cantidad de filas    | Mas columnas |
# | `np.vstack()` | Agrega **fila(s)**    | Misma cantidad de columnas | Mas filas    |
