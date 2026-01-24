arr = ["Hello", 1, 2, 3.1, True, False]

print(len(arr))

arr2 = ["Davit","Nika","Luka","Daisy","Abby"]
name = str(input("Input your name! "))
arr2.append(name)
print(arr2)

arr2.insert(3, "Tarieli")
print(arr2)

arr2.pop(4)
print(arr2)

arr2.remove("Davit")
print(arr2)

name = input("Input your name! ")

if name in arr2:
    index = arr2.index(name)
    print(f"Name {name} is in the list")
else:
    print(f"Name {name} is not in the list")

numbers = [1, 2, 3, 4, 5]


for i in range(5):
    num = int(input("Input a number to index "))
    numbers.append(num)

print(numbers)