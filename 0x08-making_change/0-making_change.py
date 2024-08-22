#!/usr/bin/python3
""" Coin Change Problem. """

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount `total`.
    
    param coins: List of the values of the coins in your possession.
    param total: The target amount to achieve using the coins.
    return: Fewest number of coins needed to meet total, or -1 if it is not possible.
    """
    if total <= 0:
        return 0
    
    # Initialize the DP table where dp[i] represents the fewest number of coins to get amount i
    fewest_coins = [float('inf')] * (total + 1)
    fewest_coins[0] = 0
    
    # Build the DP table
    for coin in coins:
        for amount in range(coin, total + 1):
            fewest_coins[amount] = min(fewest_coins[amount], fewest_coins[amount - coin] + 1)
    
    # Return the result for the desired amount
    return fewest_coins[total] if fewest_coins[total] != float('inf') else -1

