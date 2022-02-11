#1
def func():
    print('Hello World!')

func()

#2
def func1(name):
    print('Hi my name is ' + name)

func1('Elias')

#3
def func3(x, y, z):
    if z == True:
        return x
    elif z == False:
        return y

print(func3("hello", "goodbye", False))

#4
def func4(x, y): 
    return x * y

print(func4(3,4))

#5
def func5(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(func5(4))

#6
def func6(a, b):
    if a > b:
        return True
    else:
        return False
    
print(func6(3,5))

#7
def func7(*args):
    total = 0
    for x in args:
        total += x
    return total

print(func7(1,2,3,4,5,6,7,8,9))

#8
def func8(*args):
    lst = []
    for x in args:
        if x % 2 == 0:
            lst.append(x)
        else:
            pass
    return lst

print(func8(1,2,3,4,5,6,7,8))

#9
def func9(a):
    ret = ""
    i = True
    for char in a:
        if i: 
            ret += char.upper()
        else: 
            ret += char.lower()
        if char != ' ':
            i = not i
    return ret

print(func9('hella'))

#10
def func10(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return "<"
    if a % 2 != 0 or b %2 != 0:
        return ">"

print(func10(2,4))

#11
def func11(c,d):
    if c[0] == d[0]:
        return True

print(func11("yes", "yeti"))

#12
def num(a):
    return 7 - (a * 2)

print(num(3))

#13

def char(a):
    lst = list(a)
    lst[0] = lst[0].upper()
    lst[3] = lst[3].upper()

    return ''.join(lst)

print(char("hello"))
        

