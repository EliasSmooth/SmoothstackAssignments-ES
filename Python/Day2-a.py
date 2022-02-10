#1
hw = "Hello World"
r = hw[8]

print(r)

#2
t = "thinker"
ink = t[2:5]

print(ink)

#3
h = "hello"
s = "Sammy"
h_out = h[1]
s_out = s[2:]

print(h_out)
print(s_out)

#4
m = "Mississippi"
parse_m = list(m)

print(parse_m)

#5
p = ["Stats", "Amore, Roma", "No 'x' in Nixon", "Was it a cat I saw", "gore"]
form = []
a = []

for x in p:
    n = x.replace(" ", "")
    ne = n.replace("'", "")
    new = ne.replace(",", "").lower()
    form.append(new)
    
for x in form:
    if x[0:] == x[::-1]:
        a.append("Y")
    if x[0:] != x[::-1]:
        a.append("N")


print(a)


