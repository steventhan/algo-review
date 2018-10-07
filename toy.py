# Complete the missingWords function below.
def missingWords(s, t):
    s = s.split(" ")
    t = t.split(" ")
    memo = [[0]*(len(s)+1) for i in range(len(t)+1)]
    longest_sub = set()
    for i in range(len(memo)):
        for j in range(len(memo[i])):
            if i != 0 and j != 0:
                if t[i-1] == s[j-1]:
                    longest_sub.add(t[i-1])
                    memo[i][j] = memo[i-1][j-1] + 1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    print(longest_sub)
    return [word for word in s if word not in longest_sub]
