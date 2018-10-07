def solution(A, B):
    # write your code in Python 3.6
    card_val = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
        "9": 9,
        "8": 8,
        "7": 7,
        "6": 6,
        "5": 5,
        "4": 4,
        "3": 3,
        "2": 2
    }

    a_score = 0
    for i, card in enumerate(A):
        a_score += 1 if card_val[card] > card_val[B[i]] else 0
    return a_score    
