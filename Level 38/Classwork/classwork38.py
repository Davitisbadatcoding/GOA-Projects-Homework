sentence = input("Input a sentence ")
sentence_abolisher = sentence.split(" ")

for i in sentence_abolisher:
    print(i)

arr = ['hi', 'hello', '84', '16']
symbols = input("Input a symbol to add to every element ")

symbol_twined = symbols.join(arr)

print(symbol_twined)