def solution(A, K):
    N = len(A)
    B = [None] * N

    for i in range(N):
        j = ( i + K ) % N
        B[j] = A[i]

    return B

A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))