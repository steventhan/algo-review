memo = {}
def coin_change(denominations, amount):
    # import pdb; pdb.set_trace()
    if amount in denominations:
        return 1
    if amount in memo:
        return memo[amount]
    min_coins = float("inf")
    for denom in denominations:
        if denom < amount:
            min_coins = min(min_coins, coin_change(denominations, amount-denom) + coin_change(denominations, denom))
    memo[amount] = min_coins
    return min_coins

print(coin_change([1, 2, 5], 200))
