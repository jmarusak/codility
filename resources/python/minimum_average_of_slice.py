def consec_sum(A):
    n = len(A)
    P = [0] * (n + 1)
    for i in range(1, n + 1):
        P[i] = P[i-1] + A[i-1]
    return P

def solution(A):
    n = len(A)

    P = consec_sum(A)

    min_avg = float('inf')
    min_index = 0
    for i in range(1, len(P)):
        for j in range(i+1, len(P)):
            sum = P[j] - P[i-1]
            count = (j-i+1)
            avg = sum / count
            if avg < min_avg:
                min_avg = avg
                min_index = i-1
            
    return min_index 

A = [4,2,2,5,1,5,8]
print(solution(A))