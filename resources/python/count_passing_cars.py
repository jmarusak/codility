def slice_sum(P, x, y):
    return P[y + 1] - P[x]

def prefix_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = P[i - 1] + A[i - 1]        

    return P

def solution(A):
    P = prefix_sum(A)

    passing_count = 0
    for i in range(len(A)):
        if A[i] == 0:
            passing_count += slice_sum(P, i, len(A)-1)

    if passing_count > 1000000000:
        return -1
    return passing_count 

A = [0,1,0,1,1]
P = solution(A)
print(P)