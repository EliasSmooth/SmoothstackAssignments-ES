#1
l = [1, "hello", 12.4]

print(l)

#2
n = [1,1,[1,2]]

print(n[2][1])



#3
lst = ["a", "b", "c"]
lst_out = lst[1:]

print(lst_out)

#4
week = {"Sunday": 0, "Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6}

#5
d = {'k1': [1,2,3]}
d_out = d['k1'][1]

print(d_out)

#6
lt = [1,[2,3]]

imutable = tuple(lt)
#Appending results in error

#7
m = "Mississippi"
parse_m = list(m)

print(parse_m)

#8
parse_m.append('X')

print(parse_m)

#9
#a
r = range(1999, 3201)
final = []

for x in r:
    m = x % 7
    d = x % 5

    if m == 0 and d != 5:
        final.append(x)

print(final)

#b
def fact(x):
    if x == 0:
        return 1
    return x * fact(x-1)

x= 12

print(fact(x))

#c
n = 3
d = dict()

for i in range(1, n + 1):
    d[i]=i*i

print(d)

#d 
v = "34,67,55,33,12,80"

l = v.split(",")
t=tuple(l)

print(l)
print(t)

#e
class InputOutString(object):
    def __init__(self) -> None:
        self.s=""
    
    def getString(self):
        self.s = "Wozers"

    def printString(self):
        print(self.s)

strObj = InputOutString()
strObj.getString()
strObj.printString()