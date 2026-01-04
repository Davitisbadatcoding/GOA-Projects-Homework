numbers = [10, 20, 30, 40, 50]

sum_result = 0
count = 0 

for num in numbers:
    sum_result += num
    count += 1

average = sum_result / count 

print("All the numbers added up:", sum_result)
print("Average of the numbers:", average)

my_number = 12
while True:
    num = int(input("Input the number i'm thinking about! "))

    if num == my_number:
        print("Correct!")
        break
    else:
        print("Try again")
        continue

while True:
    number = int(input("input an even number!! "))

    if number % 2 == 0:  
        print("Number is Even, good job")
        break  
    else:
        print("Number is odd, try again butter fingers")
        continue 