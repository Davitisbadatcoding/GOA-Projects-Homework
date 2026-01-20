numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i in numbers:
    print(i)

total = 0
for num in numbers:
    total += num
    print(total)


even_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
print("Theres:", even_count," even numbers in the list")

min_value = numbers[0]

for num in numbers:
    if num < min_value:
        min_value = num

print("Smallest element:", min_value)

max_value = numbers[0]

for num in numbers:
    if num > max_value:
        max_value = num

print("Largest element:", max_value)

total = 0
while True:
    number = int(input("Input a number (and input 0 to stop) "))
    if number == 0:
        break
    total += number
print("All your inputed numbers added up is: ", total)

while True:
    num = int(input("Input a number "))
    if num > 0:
        print("Try Again")
    elif num == 0:
        print("Try Again")
    else:
        print("You inputed a negative number!")

while True:
    num = int(input("Input a number "))
    if num % 5 == 0:
        print("You inputed a number that can divide by 5!")
        break
    else:
        print("Try Again")

attempts = 0
while True:
    num = int(input("Input an even number "))
    if num % 2 == 0:
        print("You inputed an even number!")
        print("It took you:", attempts, "attempts!")
        break
    else:
        print("Try Again!")
        attempts += 1

while True:
    num = int(input("Input an odd number "))
    if num % 2 == 0:
        print("Try Again")
        break
    else:
        print("You inputed a odd number!")

while True:
    num = int(input("Input a number "))
    if num == 0:
        print("Good job, you entered the number 0!")
        break
    else:
        continue

while True:
    num = int(input("Input a number "))
    if num == 100:
        print("Good job, you entered the number 100!")
        break
    else:
        continue