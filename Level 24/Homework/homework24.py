num = int(input("Input a number "))
if num > 0:
    if num % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")

condition = True

while condition:
    num = int(input("Enter Number: "))

    if num <0:
        print("Number is negative")
        condition = False
    else:
        print("Number " + str(num) + " is negative! TRY AGAIN")

count = 3

while count > 0:
    pin = int(input("Enter pin: "))

    if pin == 1234:
        print("PinCode is Correct")
        count = 0
    else:
        count -= 1
        print("PinCode is Denied " + str(count) + " attempts Left")

fruits = ["apple", "banana", "peach", "pear", "cherry"]
print(fruits[2])

numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
print(numbers)

colors = ["red", "green", "blue", "yellow", "purple"]
index = int(input("Enter an index (0 to 4): "))
print(colors[index])

animals = ["dog", "cat", "elephant", "tiger", "lion"]
animals[-1] = "ship"
print(animals)

colors = ["white", "black", "orange", "pink"]
index = int(input("Enter an index (0 to 3): "))
new_color = input("Enter a new color: ")
colors[index] = new_color
print(colors)