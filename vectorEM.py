def dotproduct(a, b):
    dot = 0
    for i in range(len(a)):
        dot += float(a[i])*float(b[i])
    return dot

def crossproduct(a, b):
    a.append(a[0])
    a.append(a[1])
    b.append(b[0])
    b.append(b[1])
    cross = []
    for i in range(1, len(a)-1):
        cross.append(a[i]*b[i+1] - b[i]*a[i+1])
    return cross

def vectorsum(a, b):
    sum = []
    for i in range(len(a)):
        sum.append(float(a[i]) + float(b[i]))
    return sum    
