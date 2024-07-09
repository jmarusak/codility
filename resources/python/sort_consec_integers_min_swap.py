def solution(A):
    swaps = 0
    size = len(A)

    nodeMap = {}
    for i in range(1, size+1):
        nodeMap[i] = A[i-1]

    isVisited = [False for i in range(1, size+2)]

    for k in range(1, size+1):        
        if isVisited[k] == False:
            isVisited[k] = True

            if nodeMap[k] == k:
                continue
            else:
                c = nodeMap[k]
                while(isVisited[c] == False):
                    isVisited[c] = True
                    c = nodeMap[c]
                    swaps += 1

    return swaps


# test case
A = [5, 4, 3, 2, 1]
print(solution(A))
