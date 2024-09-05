#!/usr/bin/python3
""" Module for solving the prime game question """

def isWinner(x, nums):
    """Determines the winner of the prime game.
    
    Args:
        x: Number of rounds.
        nums: List of numbers for each round.
    
    Returns:
        The winner's name ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    # Find the maximum number in nums to limit the sieve size
    max_num = max(nums)

    # Create a prime filter list using the Sieve of Eratosthenes
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    # Mark non-prime numbers in the sieve
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    # Prepare a prime count list: prime_count[i] holds the number of primes <= i
    prime_count = [0] * (max_num + 1)
    count = 0
    for i in range(1, max_num + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    # Determine how many rounds Maria wins (prime count % 2 == 1 means Maria wins)
    maria_wins = 0
    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1

    # Determine the winner based on the number of rounds Maria wins
    if maria_wins * 2 == len(nums):
        return None  # It's a tie
    elif maria_wins * 2 > len(nums):
        return "Maria"  # Maria wins
    else:
        return "Ben"  # Ben wins
