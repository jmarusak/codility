def solution(A):
    count = 0
    n = len(A)
    increments = [A[i] - A[i - 1] for i in range(1, len(A))]

    print(increments)

    count = 0

    for i in range(len(increments)):
        for j in range(i+1, len(increments)):
            if increments[i] == increments[j]:
                count += 1
            else:
                break
    
    if count > 1000000000:
        return -1

    return count

A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]
print(solution(A))