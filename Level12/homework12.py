#shedarebit operatorebshi aris >, <, <=, >= da ==

print(10>21)
print(10>10)
print(124>2)
print(2333>2334)
print(426>325.00011)

print(213<468)
print(345<890)
print(879890<123)
print(120<120)
print(1246.6780<123434.344444444)

print(10<=700)
print(10<=10)
print(2345<=5699)
print(429<=334891)
print(213.6317<=3.999)

print(213>=2145456)
print(1234>=237874)
print(1>=1)
print(1268>=32667989)
print(124.99999>=12668.0094256)


#logical operatorebshi aris or da and -isgan shemdgari, chven shegvizlia gamoviyenot roca gvinda boolean valuebis an pasuxebis sheadareba


print(True and False) #=False
print(True and True) #=True
print(False and False) #=False


print(True or False) #=True
print(True or True) #=True
print(False or False) #=False

a = int(input("Is your number more then my mysterious number? "))
b = 14
print("Using" + str(">"))
print( a>b )
print("Using" + str("<"))
print( a<b )

c = input("Input Your Name! (With Uppercase preferably) And we will see if it's the same as mine ")
d = "Davit"
print( c==d )
print( c== "Davit")

a1 = int(input("Input your Age! "))
b1 = 18
print("Are you less then 18 of age?")
print(a1<b1)
print("Are you bigger (Older) then 18 of age?")
print(a1>b1)