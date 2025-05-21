#!/usr/bin/env python3
#HELLO AMIGUITOS DE YUTU
#THIS IS THE WAY TO CREATE COMMENTS
 # ctrl k+c comenta y k+u quita comentario(en bloques)
print("This is my first message.")

variable1=12
variable2=12.0
variable3=True
variable4=False
variable5='DAYANA BENALCAZAR'

print(variable1)
print(variable2)
print(variable3)
print(variable4)
print(variable5)

#List
print('#Lista')
list1=[1,2,3,4,5,6,7, 'Dayana',True]
print(list1[5])
print(list1[6])

#Diccionary
print('#Diccionario')
dict1={'student1':'kevin', 'student2': 'sheily'}
print(dict1['student1'])

stringVariable='3'
print(type(stringVariable))
numericalVariable=int(stringVariable)
print(type(numericalVariable))


print('------------------------')
print("CONTROL FLOW")

age=30
message1='you are younger'
message2='you are old'

if age>=25:
    print(message2)
else:
    print(message1)


if age>30:
    print(message2)
elif age<30:
    print(message1)
elif age==30:
    print('you have th right age, congratulations')


print('-----------------')
for i in list1:
    print('Elements inside the list',i)


print('how to iterate in dictionary')
for key in dict1:
    print(dict1[key])


print('-----------------')
print('FUNCTIONS')


def message():
    print('HELLO FROM THE FUNCTION MESSAGE')

message()
for i in range(10):
    message()


# name=input('Enter your name: ')
# age=int(input('Enter your age: '))

# def message1(age, name):
#     print("You are young")
#     print(f'Your name is {name} and your age is{age}')

# def message2(age,name):
#     print("You are old")
#     print(f'Your name is {name} and your age is{age}')

# def message3(age,name):
#     print("You are in the riht age")
#     print(f'Your name is {name} and your age is{age}')


# if age<30:
#     message1(age,name)
# elif age>30:
#     message2(age,name)
# else:
#     message3(age,name)

# while True:
#     name = input('Enter your name: ')
#     age = int(input('Enter your age: '))

#     def message1(age, name):
#         print("You are young !!!")
#         print(f'Your name is {name} and your age is {age}')

#     def message2(age, name):
#         print("You are old !!!")
#         print(f'Your name is {name} and your age is {age}')

#     def message3(age, name):
#         print("You are young !!!")
#         print("You are old !!!")
#         print(f'Your name is {name} and your age is {age}')

#     if age < 30:
#         message1(age, name)
#     elif age > 50:
#         message2(age, name)
#     else:
#         message3(age, name)

list1=[1,2,3,4,5]
listsquared=[]

for item in list1:
    listsquared.append (item**2)

for item in listsquared:
    print(item)


import math
listsquarenumber=[]

for item in list1:
    listsquarenumber.append(math.sqrt(item))

print('SQUARE ROOT')
for i in listsquarenumber:
    print(i)