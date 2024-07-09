def arithmetic_sequence_sum(num):
    return int((num * (num + 1)) / 2)

def solution(A):
    stable_periods = 0
    stable_periods_total = 0
    movement_prev = None

    for K in range( len(A)-1 ):
        movement = A[K+1] - A[K]
        if movement == movement_prev:
            stable_periods += 1
        else:
            stable_periods_total += arithmetic_sequence_sum(stable_periods)       
            stable_periods = 0
        movement_prev = movement
    
    stable_periods_total += arithmetic_sequence_sum(stable_periods)       
    return stable_periods_total

#A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0]  #output 5
A = [2] * 10000   #output 49985001
print(solution(A))
