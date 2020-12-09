def zeros_matrix(rows, cols):
    A = []
    for i in range(rows):
        A.append([])
        for j in range(cols):
            A[-1].append(0.0)

    return A

def matrix_multiply(A,B):
    rowsA = len(A)
    colsA = len(A[0])

    rowsB = len(B)
    colsB = len(B[0])

    C = zeros_matrix(rowsA, colsB)

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += A[i][ii] * B[ii][j]
            C[i][j] = total

    return C

def transposeMatrix(m):
    trans = m.copy()
    for i in range(len(m)):
        for j in range(len(m[0])):
            trans[j][i] = m[i][j]
    return trans

def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m, 0, c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

def solution(m):
    # Your code here
    # algorithm will calculate =>  w = v(I - A)^-1

    # find A
    A = m.copy()
    for state in range(len(A)):
        sumState = sum(A[state])
        if sumState:
            for p in range(len(A[state])):
                A[state][p] /= sumState

    # find initial state vector v
    v = [[]]
    for state in range(len(A)):
        if state == 0:
            v[0].append(1)
        else:
            v[0].append(0)

    # find (I - A)
    subMat = A.copy()
    for state in range(len(A)):
        for p in range(len(A)):
            if state == p:
                A[state][p] = 1 - A[state][p]
            else:
                A[state][p] = - A[state][p]

    subMatInv = getMatrixInverse(subMat)
    w = matrix_multiply(v, subMatInv)
    return w

print(solution([
    [0, 1, 0, 0, 0, 1],
    [4, 0, 0, 3, 2, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]))

print(solution([
    [0, 2, 1, 0, 0],
    [0, 0, 0, 3, 4],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]))

"""
# find inverse of (I - A)
    n = len(subMat)
    subMatInv = subMat.copy()
    indices = list(range(n))
    for fd in range(n):
        fdScaler = 1.0 / subMatInv[fd][fd]
        for j in range(n):
            subMatInv[fd][j] *= fdScaler
        for i in indices[0:fd] + indices[fd + 1:]:
            crScaler = subMatInv[i][fd]
            for j in range(n):
                subMatInv[i][j] = subMatInv[i][j] - crScaler * subMatInv[fd][j]

    # multiply v and (I-A)^-1 to find w
    w = [[]]
    for row in range(len(v[0])):
        w[0].append(0)

    rowsA = len(v)
    colsA = len(v[0])

    rowsB = len(subMatInv)
    colsB = len(subMatInv[0])

    for i in range(rowsA):
        for j in range(colsB):
            total = 0
            for ii in range(colsA):
                total += v[i][ii] * subMatInv[ii][j]
            w[i][j] = total

    return w
"""