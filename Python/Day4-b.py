#2
order = [34587, 98762, 77226, 88112] 
title = ["Learning Python, Mark Lutz", "Programming Python, Mark Lutz", "Head First Python, Paul Barry", "Einführung in Python3, Bernd Klein"]	
quantity = [4, 5, 3, 3]
price = [40.95, 56.80, 32.95, 24.99]

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

    
print(list(map(accRout, order, price, quantity, price)))

