def solution(x, y):
    # Your code here
    M = int(x)
    F = int(y)

    gen = 0
    while M != F and M*F > 0:
        if M > F:
            temp = (M - F)//F + ((M - F) % F != 0)
            gen += temp
            M -= temp*F
        elif F > M:
            temp = (F - M)//M + ((F - M) % M != 0)
            gen += temp
            F -= temp*M

    if (M, F) == (1, 1):
        return str(gen)
    else:
        return 'impossible'


print(solution('4', '7'))  # 4
print(solution('2', '1'))  # 1
print(solution('2', '4'))  # impossible
print(solution('16', '5'))
