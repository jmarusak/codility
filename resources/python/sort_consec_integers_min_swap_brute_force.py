def solution(A):
    swaps = 0

    # loop through each element of the array
    size = len(A)
    for ind in range(size):
        min_index = ind
 
        # select the minimum element in every iteration
        for j in range(ind + 1, size):
            if A[j] < A[min_index]:
                min_index = j
 
         # swapping the elements to sort the array
        if min_index != ind:
            #(A[ind], A[min_index]) = (A[min_index], A[ind])
            swaps += 1
    return swaps
 

# test case
A = [3, 4, 2, 1]
print(solution(A))