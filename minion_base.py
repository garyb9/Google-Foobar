def solution(n, b):
    #Your code here
    results = []
    cycle = []
    while True:
        k = len(n)
        nChars = [char for char in n]
        nChars.sort(key=int, reverse=True)
        x = int(''.join(nChars), base=b)
        nChars.sort(key=int, reverse=False)
        y = int(''.join(nChars), base=b)

        z = x - y

        digits = []
        if z == 0:
            z = '0'
        else:
            while z:
                digits.append(int(z % b))
                z //= b
            digits = digits[::-1]
        z = ''
        for dig in digits:
            z += str(dig)
        if len(z) < k:
            z = '0'*(k-len(z)) + z

        n = z
        if z not in results:
            results.append(z)
        else:
            if z not in cycle:
                cycle.append(z)
            else:
                return len(cycle)


print(solution('1211', 10))
print(solution('210022', 3))

"""
print(results)
print(cycle)
step += 1
if step == 20:
    break
"""