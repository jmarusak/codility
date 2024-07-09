def solution(S, P, Q):
    N = len(S)
    
    # Create an array to store cumulative counts of each nucleotide
    cumulative_counts = [[0] * 4 for _ in range(N + 1)]

    # Initialize the cumulative counts
    for i in range(1, N + 1):
        cumulative_counts[i] = cumulative_counts[i - 1][:]  # Copy the previous counts
        if S[i - 1] == 'A':
            cumulative_counts[i][0] += 1
        elif S[i - 1] == 'C':
            cumulative_counts[i][1] += 1
        elif S[i - 1] == 'G':
            cumulative_counts[i][2] += 1
        elif S[i - 1] == 'T':
            cumulative_counts[i][3] += 1

    # Process queries
    M = len(P)
    result = []

    for k in range(M):
        start_position = P[k]
        end_position = Q[k] + 1  # Adding 1 to include the end position

        # Check the occurrence of each nucleotide in the specified range
        for nucleotide in range(4):
            if cumulative_counts[end_position][nucleotide] - cumulative_counts[start_position][nucleotide] > 0:
                result.append(nucleotide + 1)  # Add 1 to convert index to impact factor
                break

    return result

# Example usage:
S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
print(solution(S, P, Q))  # Output: [2, 4, 1]
