def letter_combinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if digits == "":
        return []

    if len(digits) == 1:
        return list(mapping[digits])

    rest = letter_combinations(digits[1:])
    result = []
    for ch in mapping[digits[0]]:
        for combination in rest:
            result.append(ch+combination)
    return result
