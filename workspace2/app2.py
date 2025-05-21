import numpy as np 

a=np.array([1,2,3,4,5])

#shape signfica formato
print(a.shape)
print('Element extracted of index 2:', a[2])

b=np.array([[1,2,3],[11,22,33]])
print(b.shape)
print('Element extracted of index 1 and colunm 2 :', b[1,2])



print(b)

print ("Ok !!!")


c=np.zeros((5,4))
print("The matrix x is: ")
print(c)


d=np.ones((3,4))
print("Matrix of values ones: ")
print(d)

e=np.full((3,4),8)
print("Matrix of a unique values")
print(e)


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

print("\nMatriz después de agregar 200 a 1, 5 y 9:")
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