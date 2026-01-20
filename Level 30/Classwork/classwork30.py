name = str(input("Input your name "))

print(name.upper())

print(name.lower())

print(name.capitalize())

word = "example"
symbol = input("Input a symbol: ")

if symbol in word:
    index = word.index(symbol)
    print(f"{symbol} - {index}")
else:
    print("This symbol is not in word")

name = "Davit"
print(len(name))

name = str(input("Input your name: "))
if name.lower().startswith("g"):
    print("Name Starts with a g")
else:
    print("Name doesnt start with a g")

if name.lower().endswith("l"):
    print("Name Starts with a l")
else:
    print("Name doesnt start with a l")
