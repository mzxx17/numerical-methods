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

#   Tich phan chinh xac cho polynomials

def polyintegrate(f, a, b):

    sp = 0

    for i in range(len(f)):

        index = len(f) - 1 - i
        index1 = index + 1
        sp += f[i]/(index1)*((b)**(index1) - (a)**(index1))

    return sp

#   Chia doi
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

#   Newton
def newton(f, x, d = 1e-6, n = 50, rng = 5000):

    dem = 0

    while True:

        xprev = x
        dfx = df(f, x)
        val = polyval(f, x)

        if rng*abs(dfx) < abs(val):
            
            return 'Dao ham bang 0'

        else:

            x = xprev - (val)/(dfx)
            delta = x - xprev
            dem += 1

            print(f'Sai so lan lap thu {dem} la: {delta}')

            if abs(delta) <= d:

                break

            elif dem > n:

                return 'Phuong phap that bai'

    return x, dem

#   Trapezoid
def trapezoid(f, a, b, n = 10000):

    if n <= 0:
        return 'Buoc nhay khong hop le'

    k = (b-a)/n
    s = 0
    integ = polyintegrate(f, a, b)
    fa = polyval(f, a)

    for i in range(1, n+1):

        fn = polyval(f, a+k*(i))
        s += 0.5*(fa + fn)*k
        fa = fn

    return s

#   Simpson
def simpson(f, a, b, n = 10000):

    if (n <= 0) or (n%2 != 0):

        return 'Buoc nhay khong hop le'

    h = (b - a)/n
    fa = polyval(f, a)
    fb = polyval(f, b)
    integ = polyintegrate(f, a, b)
    s = 0

    for i in range(1, n):

        if i % 2 != 0:

            hs = 4

        else:
            
            hs = 2

        s += hs*polyval(f, a + i*h)

    s = (s + fa + fb)*(h/3)   

    return s


    