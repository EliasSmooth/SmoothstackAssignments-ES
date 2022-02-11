#2
def accRout(o, p, q, t):
    t1 = (o, p, q, t)
    x = lambda q : q + 10
    if p < 100:
        z = x(q)
        t2 = (o, p , z, t)
        print(t1, t2)
    else:
        t2 = (o, p, q, t)
        print(t1 , t2)

    
accRout(1200, 40.00, 4, "Gerst")

