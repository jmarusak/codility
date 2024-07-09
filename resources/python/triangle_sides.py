def solution(A):
    n = len(A)
    S = sorted(A)
    for i in range(2, n):
        if S[i-1] + S[i-2] > S[i]:
            return 1
    return 0

A = [10,2,5,1,8,20]
print(solution(A))