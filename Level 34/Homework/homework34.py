# custom functions aris chveni gaketebuli funkcia, romelic rac gvinda gavaketebt, is ketdeba def-it mere funkciis saxeli, mere frchxilebi da frchxilebshi argument, (Optional retrun boloshi)

num1 = int(input("Input your first number here "))
num2 = int(input("Input your second number here "))

def add(num1_1, num2_2):
    return num1/num2

print(add(num1, num2))

num3 = int(input("Input a number to check if its even or odd "))

def even_odd(num3_3):
    if num3_3 % 2 == 0:
        print("Even")
    else:
        print("Odd")
        return
    
print(even_odd(num3))

num4 = int(input("Input a number to square "))

def squared(num4_4):
        return num4_4 ** 2
    
print(squared(num4))

word1 = input("Input anything you'd like ")

def uppercase(word1_1):
     return word1_1.upper()
print(uppercase(word1))

name = input("Input your name ")
last_name = input("Input your lastname ")

def username(user_username, user_userlastname):
     return f"{user_username}_{user_userlastname}"

print(username(name, last_name))