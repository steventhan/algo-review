def longest_common_substring(s1, s2):
    if not s1 or not s2:
        return 0

    if s1[-1] != s2[-1]:
        return longest_common_substring(s1[:-1], s2[:-1])
    else:
        return 1 + longest_common_substring(s1[:-1], s2[:-1])