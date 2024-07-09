def solution(A):
    positive = set(x for x in A if x>0)
    if not positive:
        return 1

    max_positive = max(positive)
    for N in range(1, max_positive + 2):
        if N not in positive:
            return N

A = [1, 3]
print(solution(A))