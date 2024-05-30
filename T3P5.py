def min_difference(mangoes, M):
    # Step 1: Sort the list of mangoes
    mangoes.sort()
    
    # Initialize the minimum difference to a large value
    min_diff = float('inf')
    
    # Step 2: Find the minimum difference in any subarray of size M
    for i in range(len(mangoes) - M + 1):
        diff = mangoes[i + M - 1] - mangoes[i]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff

# Example usage:
mangoes = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
M = 7
print(min_difference(mangoes, M))