# def isosceles(b,h):
#   return(b*h)/2
# b=int(input("enter the number "))
# h=int(input("enter the number "))
# print(isocelestri(b,h))

# def rightangled(a,b):
#   return(a*b)/2
# a=int(input("enter the number "))
# b=int(input("enter the number "))
# print(rightangle(a,b))
   
# def equilateral(a):
#   return (a * a) * (3 **0.5) * 0.25
# a=int(input("enter the number "))
# print(equilateral(a))

def printArea(area):
    print("",end='\n')
    print(f'{area} sq units is the area')

def rightAngledTriangle():
    b = int(input("Enter base:"))
    h = int(input("Enter height:"))
    printArea(0.5 * b * h)


def scalenetriangle():
    b = int(input("Enter base: "))
    h = int(input("Enter height: "))
    area = 0.5 * b * h
    printArea(area)

def equilateralTriangle():
    a = int(input("Enter side:"))
    printArea((a * a) * (3 **0.5) * 0.25)

while(True):
    print("Welcome to menu driven program:\n")
    print("1. Right angled triangle")
    print("2. Scalene triangle")
    print("3. Equilateral triangle\n")
    choice = int(input("Enter your choice:"))
    print("~")
    if choice == 1:
        rightAngledTriangle()
    elif choice == 2:
        scaleneTriangle()
    elif choice == 3:
        equilateralTriangle()
    repeat = input("Do you want to continue?:")
    if(repeat != 'yes'):
        break
