#!/usr/bin/python3
"""Making change """

def make_change_greedy(coins, target_amount):
    if target_amount <= 0:
        return 0
    
    coins.sort(reverse=True)
    total_coins_used = 0

    for coin_value in coins:
        if target_amount <= 0:
            break
        num_coins = target_amount // coin_value
        total_coins_used += num_coins
        target_amount -= (num_coins * coin_value)

    if target_amount != 0:
        return -1

    return total_coins_used

