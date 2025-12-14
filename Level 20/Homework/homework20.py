num1 = int(input("Input a number "))
if num1 > 10:
    print("More then Ten")
elif num1 == 10:
    print("Is equal to Ten")
else:
    print("Less then Ten")

num2 = int(input("Input another number "))
if num2 == 15:
   print(str(num2) + " is equal to 15") 
else:
       print(str(num2) + " is not equal to 15")

word1 = input("Input your group number: ")
group = "Group 84"
if word1 == group:
    print("You are absolutley correct")
else:
    print("Nope you aren't")

for i in range(50, 100, 5):
    print(i)

name = "Davit"
last_name = "Patarkartsishvili"
for o in range(3):
    print( name + " " + last_name )

num3 = 20
while num3 < 50:
    print(num3)
    num3 += 1

zero = 0
hundred = 100
for p in range(zero, hundred):
    print(p)

while zero < hundred:
    print(zero)
    zero += 1

hundredone = 101
for p in range(zero, hundredone):
    print(p)

while zero < hundredone:
    print(zero)
    zero += 1

for a in range(10, 20):
    print(a)

ten = 10
while ten < 20:
    print(ten)
    ten += 1

for s in range(100, 201 , 5):
    print(s)

hundred = 100
while hundred <= 200:
    print(hundred)
    hundred += 5

for d in range(10, 0, -1):
    print(d)

while ten > zero:
    print(ten)
    ten -= 1

num4 = input("Input a number ")
if int(num4) > 0:
    print("Your number is positive")
elif int(num4) == 0:
    print("Your number is equal to 0")
else:
    print("Your number is negative")

age = int(input("Input Your Age "))
if age <0:
    print("Liar")
elif 0 <= age <= 12:
    print("You are a kid")
elif 13 <= age <= 19:
    print("You are a teen")
elif 20 <= age <= 64:
    print("You are an adult")
elif 65 <= age <= 120:
    print("You are a grampa")
else:
    print("Dont choke on air gramps...")

num5 = float(input("Input a number "))
num6 = float(input("Input another number "))
num7 = float(input("Last number i swear "))
if num5 >= num6 and num5 >= num7:
    print("Biggest number is: ", num5)
elif num6 >= num5 and num6 >= num7:
    print("Biggest number is: ", num6)
else:
    print("Biggest number is: ", num7)

num8 = int(input("Input a number corresponding to a day of the week (So many numbers..) "))
if num8 == 1:
    print("Monday")
elif num8 == 2:
    print("Tuesday")
elif num8 == 3:
    print("Wednesday")
elif num8 == 4:
    print("Thursday")
elif num8 == 5:
    print("Friday")
elif num8 == 6:
    print("Saturday")
elif num8 == 7:
    print("Sunday")
else:
    print("There isnt more then 7 days of the week... Try again..")

num9 = int(input("Input more numbers "))
if num9 >= 50:
    print(num9 * 50)
else:
    print(num9 ** 2)

word2 = input("Input your password ")
password = "goa123"
if word2 == password:
    print("Password is correct")
else:
    print("Password is incorrect, try again")

num10 = int(input("Input the last number of them all "))
zero = 0
one = 1
while one <= num10:
    zero += one
    one += 1

print(zero)