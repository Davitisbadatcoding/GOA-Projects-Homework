def greet(name):
    print("Hello World")
    print(f"Hello {name}")

greet("Davit")

def double(num):
    return num ** 2

num = int(input("Input a number to square "))
print(double(num))

def checkOdd(something):
    if something % 2 ==0:
        return print("Even")
    else:
        return print("Odd")
    
num2 = int(input("Input a number to check if its even or odd! "))
checkOdd(2)

def BMI(height, weight):
    return print(f"BMI --> {height/weight}")

weight = input("Input your weight ")
height = input("Input your height ")
BMI(20, 2)