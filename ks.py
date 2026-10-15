def polyval(f, x):
    v = 0
    for i in range(len(f)):
        index = len(f) - 1 - i
        v += (f[i])*((x**(index)))
    return v

def df(f, x, h = 1e-5):
    sp = 0
    for i in range(len(f)):
        index = len(f) - 1 - i
        sp += (f[i])*(((x+h)**(index)) - (x**(index)))
    return (sp/(h))

def bisection(f, a, b, d = 1e-6):

    dem = 0
    fa = polyval(f, a)
    fb = polyval(f, b)

    if (fa*fb) <= 0:

        while (b - a) > d:

            x = (a+b)/2
            fx = polyval(f, x)

            if fx*fa > 0:
                a = x
        
            else:
                b = x

            dem += 1

        return (a+b)/2, dem
    
    else: 
        return "Phuong phap khong ap dung duoc"

print(bisection([2, 2, -6], 0, 3))
