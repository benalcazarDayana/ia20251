# def prediction(age):
#     age=age+10
#     return age

# def niceMessage(agePredicted,name):
#     print(f'Your name is {name} and yuor age after 10 years is {agePredicted}')

# while True:
#     name=input("Enter your name please: ")
#     age=int(input("Enter your age "))

#     agePredicted=prediction(age)
#     niceMessage(agePredicted,name)


print('CONTAINERS LIST')

listNumbers=list()
listNumbers.append(3)
listNumbers.append(1)
listNumbers.append(2)

for item in (listNumbers):
    print(item)


#extrae un elemento
print(listNumbers[-2])


listNumbers[-2]='Dayana'
for item in (listNumbers):
    print(item)
print('-------------------------------------')

print('before pop')

listNumbers.append('bar')
for item in (listNumbers):
    print(item)

print('after pop')

lastItem=listNumbers.pop()
print("list: ", listNumbers)
print('lastITem')

print('-------------------------------------')

listNumbers1=list(range(30))
print(listNumbers1)

print('-------------------------------------')
#extrae un conjunto de elementos
itemSelected=listNumbers1[10:21]
print(itemSelected)

# itemSelectedChange=list()
# for i in itemSelected:
#     itemSelectedChange.append(i+10)
# print(itemSelectedChange)

#listNumbers1[10:21]=itemSelected+10
print('new  list')
print(listNumbers1)


print('-------------------------------------')
evenList = [i for i in range(10) if i % 2 == 0]

print(evenList)

firstList=list(range(20))
secondList=[i**2 for i in firstList]
print(firstList)
print(secondList)