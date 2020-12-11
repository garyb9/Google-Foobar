import math
import numpy as np
from fractions import Fraction

def solution(m):
    # Your code here
    if len(m) == 1:
        return [1, 1]

    # find A - probability matrix, TR - terminal states vector, ABS - absorbing states vector
    A = np.array(m).astype(float)
    TR = []
    ABS = []
    for state in range(len(A)):
        sumState = float(sum(A[state]))
        if sumState:
            A[state] = A[state] / sumState
            TR.append(state)
        else:
            ABS.append(state)

    shapeA = len(A)  # must be a square matrix

    # find fundamental matrix P
    #            TR  ABS
    #       TR  | Q | R |
    # P  =  ABS | O | I |
    qShape = len(TR)
    Q = np.zeros((qShape, qShape))
    rShape = len(ABS)
    R = np.zeros((qShape, rShape))

    for row in range(shapeA):
        if row in TR:
            qRow = []
            rRow = []
            for col in range(shapeA):
                if col in TR:
                    qRow.append(A[row][col])
                else:
                    rRow.append(A[row][col])
            Q[row] = qRow
            R[row] = rRow

    # find N = (I - Q)^-1
    IQ = np.identity(qShape) - Q
    N = np.linalg.inv(IQ)

    # find B = NR
    B = np.matmul(N, R)

    # since S0 is the only initial state, we should only parse B[0]
    nominators = []
    denominators = []
    for val in B[0]:
        nominators.append(Fraction(val).limit_denominator().numerator)
        denominators.append(Fraction(val).limit_denominator().denominator)
    # find the least common denominator
    lcd = 1
    for d in denominators:
        lcd = abs(lcd * d) // math.gcd(lcd, d)

    # rearrange nominators, add lcd and return
    for idx in range(len(nominators)):
        nominators[idx] = nominators[idx] * int(lcd/denominators[idx])
    nominators.append(lcd)

    return nominators

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