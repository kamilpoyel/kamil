fruits = ["apple","orange", "pear", "banana", "apple"]


print("rozpoczynam pentle")
for i,fruit in enumerate(fruits):
    print("sprawdzam {} ".format(i))
    if i==3:
        break
    print("{} jest ok".format(fruit))


print("koniec")

x="h3llo {} {}"
y=x.format("world", "5.5")
print(x)
print(y)
