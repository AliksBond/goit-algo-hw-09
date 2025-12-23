""" жадібний алгоритм """

def find_coins_greedy(amount):
    result = {}
    
    for coin in COINS:
        result[coin] = 0
        while amount >= coin:
            amount -= coin
            result[coin] += 1

        if result[coin] == 0:
            del result[coin]

    return result


""" динамічне програмування """

def find_min_coins(amount):
    dp = [None] * (amount + 1)
    dp[0] = {}

    for i in range(1, amount + 1):
        best_solution = None

        for coin in COINS:
            if i - coin >= 0 and dp[i - coin] is not None:
                candidate = dp[i - coin].copy()
                candidate[coin] = candidate.get(coin, 0) + 1

                if best_solution is None or sum(candidate.values()) < sum(best_solution.values()):
                    best_solution = candidate

        dp[i] = best_solution

    return dp[amount]






