def solution(A):
    # Shortcut solutions
    N = len(A)
    if len(set(A)) != N:
        return 0

    M = max(A)
    if M != N:
        return 0

    S = sum(A)
    arithmetic_sum = M * (M + 1) / 2
    if arithmetic_sum == S:
        return 1
    else:
        return 0

A1 = [4,3,1,2]
print(solution(A1))
A2 = [4,3,1]
print(solution(A2))
A3 =  [100000]
print(solution(A3))

A4 =  [1] * 1000000000
print(solution(A4))
