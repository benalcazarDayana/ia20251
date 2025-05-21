# pairs key and the other value

myDictonary={'cat':'cute','dog':'friends','donkey':'hard-working'}

print(myDictonary['donkey'])

print('cat' in myDictonary)

myDictonary['fish']='wet'

for key in myDictonary:
    value=myDictonary[key]
    print ('The %s is %s'%(key,value))

print("Another way to print dictionaries")

for key, value in myDictonary.items():
    print ('the %s is %s '%(key,value))


print ('----------------------------------------------------')
#dictionary={'1':1, '2':4.....}

myDictonary1={i:i**2 for i in range(20)}
print(myDictonary1)

# dictionary = {str(i): i**2 for i in range(1, 21)}
# for key, value in dictionary.items():
#     print(f"The {key} is {value}")

print ('----------------------------------------------------')

print ('SET CONTAINER')
animals={'cat','dog','chicken','hen','monkey'}
print('fish'in animals)
animals.add('fish')
print(animals)
animals.add('mouse')
print(animals)

print ('----------------------------------------------------')
numberOfElments=len(animals)
print(numberOfElments)

print ('----------------------------------------------------')

animals.remove('cat')
print(animals)
print(type(animals))
print(len(animals))

print ('----------------------------------------------------')

print('TUPLES')
# tupleData1=(5,5,5)
# print(type(tupleData1))



tupleData = (1,2,5)
listData = list(tupleData)
tupleData = tuple(listData)
print(tupleData)

tupleData = (1,2,5)
# Convertir a lista
listData = list(tupleData)
# Eliminar el 5 (por valor)
listData.remove(5)  # Esto solo elimina el valor 5
# Volver a convertir a tupla
tupleData = tuple(listData)
print(tupleData)
