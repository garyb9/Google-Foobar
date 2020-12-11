from fractions import Fraction, gcd

def getTRandABS(m):
    TR = []
    ABS = []
    for row in range(len(m)):
        sumState = float(sum(m[row]))
        if sumState:
            TR.append(row)
        else:
            ABS.append(row)
    return TR, ABS

def zerosMatrix(rows, cols):
    A = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(0.0)
        A.append(row)
    return A

def multiplyMatrix(A, B):
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    C = zerosMatrix(rowsA, colsB)
    if colsA == rowsB:
        for i in range(rowsA):
            for j in range(colsB):
                total = 0
                for ii in range(colsA):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total

    return C

def identityMatrix(size):
    A = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        A.append(row)
    return A

def helperMultRowSQ(m, row, k):
    n = len(m)
    opRow = identityMatrix(n)
    opRow[row][row] = k
    return multiplyMatrix(opRow, m)

def helperAddMultRowSQ(m, sRow, k, tRow):
    n = len(m)
    opRow = identityMatrix(n)
    opRow[tRow][sRow] = k
    return multiplyMatrix(opRow, m)


def invMatMatrix(A):
    n = len(A)
    invMat = identityMatrix(n)
    for col in range(n):
        diagRow = col
        k = Fraction(1, A[diagRow][col])
        A = helperMultRowSQ(A, diagRow, k)
        invMat = helperMultRowSQ(invMat, diagRow, k)
        sRow = diagRow
        for tRow in range(n):
            if sRow != tRow:
                k = -A[tRow][col]
                A = helperAddMultRowSQ(A, sRow, k, tRow)
                invMat = helperAddMultRowSQ(invMat, sRow, k, tRow)
    return invMat

def fractionMatrix(A):
    for row, rowVal in enumerate(A):
        row_sum = sum(A[row])
        if row_sum == 0:
            A[row][row] = 1
        else:
            for col, colVal in enumerate(rowVal):
                A[row][col] = Fraction(colVal, row_sum)

def getQR(A, TR):
    Q = []
    R = []

    for row in range(len(A)):
        if row in TR:
            qRow = []
            rRow = []
            for col in range(len(A)):
                if col in TR:
                    qRow.append(A[row][col])
                else:
                    rRow.append(A[row][col])
            Q.append(qRow)
            R.append(rRow)
    return Q, R


def subtractMatrix(A, B):
    C = []
    for row, rowVal in enumerate(A):
        column = []
        for col, colVal in enumerate(rowVal):
            column.append(A[row][col] - B[row][col])
        C.append(column)

    return C

def solution(m):
    # Your code here
    # find TR - terminal states vector, ABS - absorbing states vector
    TR, ABS = getTRandABS(m)

    if len(ABS) == 1:
        return [1, 1]

    # find fundamental matrix P
    #            TR  ABS
    #       TR  | Q | R |
    # P  =  ABS | O | I |
    fractionMatrix(m)
    Q, R = getQR(m, TR)

    # find N = (I - Q)^-1
    IQ = subtractMatrix(identityMatrix(len(Q)), Q)
    N = invMatMatrix(IQ)

    # find B = NR
    B = multiplyMatrix(N, R)

    # since S0 is the only initial state, we should only parse B[0]
    Nominators = []
    Denominators = []
    for val in B[0]:
        Nominators.append(val.numerator)
        Denominators.append(val.denominator)
    # find the least common denominator
    LCD = 1
    for D in Denominators:
        LCD = abs(LCD * D) // gcd(LCD, D)

    # rearrange Nominators, add lcd and return
    for idx in range(len(Nominators)):
        Nominators[idx] = Nominators[idx] * (LCD/Denominators[idx])
    Nominators.append(LCD)

    return Nominators


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