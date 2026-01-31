# append listis bolos svavs sheni mocemul data-s, insert ki romel indexzec ginda, pop ki shlis

arr = [1, 2, 3, 4, 5, 6, "Hello!"]
print(len(arr))

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
attempts = 0
while True:
    inpu = int(input("Input a Number "))
    arr2.append(inpu)
    attempts += 1
    if attempts == 5:
        print(arr2)
        break

colors = ["red", "green", "blue", "yellow", "purple"]
colors.pop(4)
print(colors)

animals = ["dog", "cat", "elephant", "lion"]
animals.insert(1, "monkey")
print(animals)

teach = ["Davit Shavidze"]
names = []
attempts = 0
while True:
    name_input = str(input("Input your classmates names! "))
    names.append(name_input)
    attempts += 1
    if attempts == 3:
        print(names)
        break

teach.insert(0, names)
names.pop(2)
print(teach)
print(len(names))
print(len(teach))