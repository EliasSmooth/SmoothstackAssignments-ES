#1
import random


r = range(1499, 2701)
a = []

for x in r: 
    d = x % 7
    m = x % 5
    if d == 0 and m == 0:
        a.append(x)

print(a)

#2
celsius = 60
fahrenheight = 45

def ftoc(f):
    print ((f-32)*5/9)

def ctof(c):
    print((60*9/5)+32)

ftoc(fahrenheight)
ctof(celsius)

#3
guess = 3

r = random.randint(0,9)

if guess == r:
    print("SUCCESS")

#4/5
t = 5

for i in range(0, t):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("")

for i in range(t, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

#6
input = 'great'
output = input[::-1]

print(output)

#7
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even = 0
odd = 0

for x in numbers:
    f = x % 2
    if f == 0:
        even += 1
    else:
        odd += 1

print(even)
print(odd)

#8
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0,-1), [5,12], {"class": 'V', "section": 'A'}]

for x in datalist:
    t = type(x)
    print(x)
    if t is str:
        print("string")
    elif t is bool:
        print("Boolean")
    elif t is list:
        print("List")
    elif t is dict:
        print("Dictionary")
    elif t is int:
        print("Integer")
    elif t is float:
        print("Float")
    elif t is complex:
        print("Complex")
    elif t is tuple:
        print("Tuple")
    

#9
r = range(0,10)

for x in r:
    if x == 3:
        continue
    elif x ==6:
        continue
    else:
        print(x)