def solution(A):
    B = sorted(A)
    print(B)

    pos = B[-3:]
    neg = B[:2]

    pos_product = pos[0] * pos[1] * pos[2]
    neg_product = neg[0] * neg[1] * pos[2]

    if pos_product > neg_product:
        return pos_product
    else:
        return neg_product


A = [-3,1,2,-2,5,6]
print(solution(A))