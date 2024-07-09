def solution(N, A):
    M = len(A)
    max_counter = 0
    temp_counter = 0
    counters = [0] * N

    for K in range(M):
        counter = A[K] - 1
        if counter < N:
            counters[counter] = max(counters[counter], max_counter) + 1 
            if counters[counter] > temp_counter:
                temp_counter = counters[counter]
        else:
            max_counter = temp_counter

    for i in range(N):
        if counters[i] < max_counter:
            counters[i] = max_counter       

    return counters

N = 5
A = [3,4,4,6,1,4,4]
print(solution(N, A))