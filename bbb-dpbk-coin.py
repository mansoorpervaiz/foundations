# Given an integer representing a given amount of change, write a function to compute the total number of coins required to make that amount of change. You can assume that there is always a 1¢ coin.
# eg. (assuming American coins: 1, 5, 10, and 25 cents)
# makeChange(1) = 1 (1)
# makeChange(6) = 2 (5 + 1)
# makeChange(49) = 7 (25 + 10 + 10 + 1 + 1 + 1 + 1)

min_coins_hash = {}

def makeChangeMemoization(amount):
    #1, 5, 10, 25
    if amount in min_coins_hash:
        return min_coins_hash[amount]
    if amount == 1:
        return 1
    if amount == 0:
        return 0

    min_coins = float('inf')

    denominations = [25, 10, 5, 1]
    for denomination in denominations:
        remainder = amount - denomination
        if remainder > 0:
            number_of_coins = makeChangeMemoization(remainder)
            if number_of_coins < min_coins:
                min_coins = number_of_coins
    min_coins_hash[amount] = min_coins + 1

    return min_coins_hash[amount]

print(makeChangeMemoization(1))
print(makeChangeMemoization(6))
print(makeChangeMemoization(49))

def makeChangeDPNoCache(amount):
    cache = [float("inf") for i in range(amount)]
    current_amount = 0
    number_of_coins = 0
    while (current_amount < amount):
        denominations = [25, 10, 5, 1]
        for denomination in denominations:
            if current_amount + denomination <= amount:
                current_amount += denomination
                number_of_coins += 1
                break


    return number_of_coins

#
print(makeChangeDPNoCache(1))
print(makeChangeDPNoCache(6))
print(makeChangeDPNoCache(49))



def makeChangeDPWTCache(amount):
    cache = [0]

    for current_amount in range(1, amount+1):
        current_min_coins = float("inf")
        denominations = [1, 5, 10, 25]
        for denomination in denominations:
            if current_amount - denomination >= 0:
                current_coins = cache[current_amount - denomination] + 1
                if current_coins < current_min_coins:
                    current_min_coins = current_coins
        cache.append(current_min_coins)
    return cache[amount]

print(makeChangeDPWTCache(1))
print(makeChangeDPWTCache(6))
print(makeChangeDPWTCache(49))

