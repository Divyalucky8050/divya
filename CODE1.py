def max_score_subarray(N, K, A):
    # Step 2: Create the score array S
    S = [(i + 1) * A[i] for i in range(N)]  # Calculate scores based on 1-based index

    # Step 3: Sliding window to find the max score for subarrays of size K
    max_score = float('-inf')
    
    # Calculate the score for the first window
    current_score = sum(S[:K])
    max_score = current_score
    
    # Slide the window
    for i in range(K, N):
        current_score += S[i] - S[i - K]  # Slide the window
        max_score = max(max_score, current_score)
    
    return max_score

# Sample input
N = 5
K = 2
A = [1, 2, 3, 4, 5]

# Function call
result = max_score_subarray(N, K, A)
print(result)  # Output the result