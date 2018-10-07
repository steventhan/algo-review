def missingWords(s, t):
    #print(longest_ddsub)
    s = s.split(" ")
    t = t.split(" ")
    longest_sub = gen_longest(s, t)
    i = 0
    j = 0
    res = []
    while i < len(longest_sub):
        print(longest_sub[i], s[j])
        if longest_sub[i] != s[j]:
            res.append(s[j])
            j += 1
        else:
            i += 1
            j += 1
    res.extend(s[j:])
    return res

def gen_longest(s, t):
    memo = [[0]*(len(s)+1) for i in range(len(t)+1)]
    ls = [[0]*(len(s)+1) for i in range(len(t)+1)]
    for i in range(len(memo)):
        for j in range(len(memo[i])):
            if i != 0 and j != 0:
                if t[i-1] == s[j-1]:
                    memo[i][j] = memo[i-1][j-1] + 1
                    ls[i][j] = "diag"
                else:
                    if memo[i-1][j] > memo[i][j-1]:
                        memo[i][j] = memo[i-1][j]
                        ls[i][j] = "up"
                    else:
                        memo[i][j] = memo[i-1][j]
                        ls[i][j] = "left"

    longest_sub = []
    while i > 0 and j > 0:
        if ls[i][j] == "diag":
            longest_sub.append(t[i-1])
            i -= 1
            j -= 1
        elif ls[i][j] == "up":
            i -= 1
        elif ls[i][j] == "left":
            j -= 1
    return longest_sub[::-1]

s = "I am using hackerrank to improve programming programming"
t = "am hackerrank to improve gibberish programming"
print(missingWords(s, t))
