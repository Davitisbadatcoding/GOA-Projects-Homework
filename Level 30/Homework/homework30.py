# .upper() yvela asos adidebs, .lower(), ki pirikit, apataravebs, .capitalize() marto pirvel aos adidebs, da danarchenbs ki apataravebs

word = str(input("Input a sentence! "))
print(word.lower())

while True:
    email = input("Input your email! ")
    if "@" in email:
        print(email.upper())
        break
    else:
        print("Try Again")

book = str(input("Input a book name! "))
print(book.capitalize())

word_input = str(input("Input any symbols you would like"))
print(word_input.find("!"))
print(word_input.find("@"))
print(word_input.find("#"))
print(word_input.find("$"))
print(word_input.find("%"))
print(word_input.find("^"))
print(word_input.find("&"))
print(word_input.find("*"))
print(word_input.find("("))
print(word_input.find(")"))
print(word_input.find("-"))
print(word_input.find("_"))
print(word_input.find("="))
print(word_input.find("+"))
print(word_input.find("`"))
print(word_input.find("~"))
print(word_input.find("["))
print(word_input.find("]"))
print(word_input.find("{"))
print(word_input.find("}"))
print(word_input.find("|"))
print(word_input.find(";"))
print(word_input.find(":"))
print(word_input.find("'"))
print(word_input.find("."))
print(word_input.find("<"))
print(word_input.find(">"))
print(word_input.find("?"))
print(word_input.find("/"))

#Simple way

sentence = input("Input a sentence! ")
symbol = input("Input a symbol! ")

count = sentence.count(symbol)
print(f"The Symbol {symbol} is seen {count} time/times")

word2 = str(input("Input a word! "))
if word2 == word2.upper():
    print("Word is already uppercase!")
else:
    print("Uppercase version:", word2.upper())