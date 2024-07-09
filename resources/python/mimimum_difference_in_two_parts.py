def solution(A):
    N = len(A)

    sum_all = 0
    for i in range(N):
        sum_all += A[i]

    sum_part1 = 0
    sum_part2 = 0
    difference_min = float('inf') 
    for i in range(N-1):
        sum_part1 += A[i]
        sum_part2 = sum_all - sum_part1
        difference = abs(sum_part1 - sum_part2)
        if difference < difference_min:
            difference_min = difference

    return difference_min 

A = [-1000, 1000]
print(solution(A))