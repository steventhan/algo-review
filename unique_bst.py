def unique_bst(n):
    memo = [1, 1]

    for i in range(2, n+1):
        total = 0
        for j in range(1, i+1):
            total += memo[i-j] * memo[j-1]
        memo.append(total)
    return memo[n]
