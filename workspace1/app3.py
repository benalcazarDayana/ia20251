# def computerAreaSquare(side):
#     return side*side

# def computerAreaCircle(radius):
#     pi=3.1415
#     return pi*radius**2

# print (f"The area of an aquare with side 3cm is {computerAreaSquare(3)}")
# print (f"The area  a circle with a radius of 3 is {computerAreaCircle(3):.2f}")


class Geometry:
    #variable de clase
    pi=3.1415
    def  __init__(self,side,radius):
        #variable de objeto
        self.side=side
        self.radius=radius
        print("The object was creates successfully")

    def area(self):
        squareArea=self.side*self.side
        circleArea=Geometry.pi*self.radius**2
        #define la funcion
        return[squareArea,circleArea]


areaSquareCircle=Geometry(3,3)
result=list()
result=areaSquareCircle.area()
print(f"The area of the square and circle area:{result[0]},{result[1]:.2f}")


print('----------------------------------')
print('RECTANGULO')
class Rectangle:
    def __init__(self, width, height):
        # Inicializa los atributos de instancia
        self.width = width
        self.height = height
        print("The object was creates successfully")
    
    def area(self):
        # Calcula el area del rectangulo
        return self.width * self.height


# Crear un objeto de la clase Rectangle
rect1 = Rectangle(5, 3)
# Mostrar el area
print(f"El area del rectangulo es: {rect1.area()} cm²")

print('----------------------------------')
print('PROMEDIO DE NOTAS')

import statistics
class Student:
    def __init__(self,name,grades):
        self.name=name
        self.grades=grades
    
    def average_grade(self):
        score=statistics.mean(self.grades)
        return score
   

dayanaStudent=Student('Dayana',[6,8,7,5])

alejandroStudent=Student('Alejandro',[6,5,10,7])

winstonStudent=Student('Winston',[8,8,7,10])

print(f"THE SCORE OF DAYANA IS {dayanaStudent.average_grade()}")
print(f"THE SCORE OF ALEJANDRO IS {alejandroStudent.average_grade()}")
print(f"THE SCORE OF WINSTON IS {winstonStudent.average_grade()}")

