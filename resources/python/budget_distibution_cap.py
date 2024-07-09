def solution(A, budget):
    size = len(A)
    split_initial = budget / size
    split_remaining = budget

    B = sorted(A)

    for i in range(size):
        if B[i] <= split_initial:
            budget -= B[i]
            split_remaining = budget / (size - i - 1)
        else:
            B[i] = split_remaining

    return split_remaining 

A = [2, 5, 100, 50, 1000]
budget = 190
print(solution(A, budget))