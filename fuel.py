"""
def solution(n):
    # Your code here
    N = int(n)
    step = 0
    while N > 1:
        # get base 2 of N into a string
        digits = []
        tempN = N
        while tempN:
            digits.append(int(tempN % 2))
            tempN //= 2
        digits = digits[::-1]
        N2 = ''
        for dig in digits:
            N2 += str(dig)

        # get length of bits in base 2
        lenN2 = len(N2)
        upper = '1'+'0'*lenN2
        lower = '1'+'0'*(lenN2 - 1)

        # get integers in base 10
        upperN = int(upper, base=2)
        lowerN = int(lower, base=2)

        if upperN == N or lowerN == N:
            return str(lenN2 - 1 + step)
        else:
            if N % 2 == 0:
                N //= 2
            else:
                if (upperN - N) < (N - lowerN):
                    N += 1
                else:
                    N -= 1
            step += 1

    return str(step)
"""

def solution(n):
    # Your code here
    N = int(n)
    if N == 1:
        return '0'
    step = 0
    while N > 1:
        if N == 2:
            return str(step + 1)
        elif N == 3:
            return str(step + 2)
        else:
            if N % 2 == 0:
                N //= 2
            else:
                if N % 4 == 1:
                    N -= 1
                else:
                    N += 1
        step += 1


for n in range(1, 1100):
    k = solution(n)
    if type(k) != str:
        print("gay")
    print(n, k)
