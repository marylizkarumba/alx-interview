#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each total value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the minimum number of coins needed for each total value
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1