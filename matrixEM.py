def mat_det(lst):
    if len(lst) == 1:
        if len(lst[0]) == 1:
            return abs(lst[0][0])
        else: 
            return None
    elif len(lst) == 2:
        if len(lst[0]) == len(lst[1]) == 2:
            return lst[0][0]*lst[1][1]-lst[1][0]*lst[0][1]
        else:
            return None
    elif len(lst) == 3:
        if len(lst[0]) == len(lst[1]) == len(lst[2]) == 3:
            det = (lst[0][0]*lst[1][1]*lst[2][2]+lst[0][1]*lst[1][2]*lst[2][0]+lst[0][2]*lst[1][0]*lst[2][1])-(lst[2][0]*lst[1][1]*lst[0][2]+lst[2][1]*lst[1][2]*lst[0][0]+lst[2][2]*lst[1][0]*lst[0][1])
            return det
        else:
            return None
    else:
        return None

mat_det([[1, 2, 3], [5, 6, 7], [-2, -3, -1]])

def mat_sum(mat1, mat2):
    if len(mat1) == len(mat2):
        if len(mat1[0]) == len(mat2[0]):
            mat = []
            for i in range(len(mat1)):
                comp = []
                for k in range(len(mat1[0])):
                    comp.append(mat1[i][k]+mat2[i][k])
                mat.append(comp)
            return mat
        else:
            return None
    else:
        return None

mat_sum([[1, 2, 3], [5, 6, 7]], [[1, 3, 5], [5, 7, 5]])

def mat_product(mat1, mat2):
    if len(mat1[0]) == len(mat2):
        mat = []
        for i in range(len(mat1)):
            comp = []
            for j in range(len(mat2[0])):
                s = 0
                for k in range(len(mat2)):
                    s += (mat1[i][k]*mat2[k][j])
                comp.append(s)
            mat.append(comp)
        return mat
    else:
        return None
    
mat_product([[1, 2], [3, 6]], [[2, 1, -3], [1, 2, 0]])

def mat_extraction(mat):
    if len(mat) == len(mat[0]):
        a = []
        for i in range(1, len(mat[0])):
            for j in range(len(mat)-i+1): # hang
                for k in range(len(mat)-i+1): # cot
                    b = [mat[j+f][k:k+i] for f in range(i)]
                    a.append(b)
        return a
    else:
        return None

print(mat_extraction([[1, 2, 3, 5], [5, 6, 7, 9], [3, -2, -3, -1], [1, 2, 3, 3, 8]]))