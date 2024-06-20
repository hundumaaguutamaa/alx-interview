#!/usr/bin/python3
""" Module solving prime game problem. """


def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben based on prime number counts.

    Args:
        x (int): A positive integer (not used in the current implementation).
        nums (List[int]): A list of positive integers.

    Returns:
        str or None: The winner ("Maria" or "Ben") or None if no winner.
    """
    if not nums or x <= 0:
        return None
    
    max_nums = max(nums)
    
    # Sieve of Eratosthenes to find all primes up to max_n
    is_prime = [True] * (max_nums + 1)
    is_prime[0] = is_prime[1] = False  
    
    p = 2
    while p * p <= max_nums:
        if is_prime[p]:
            for i in range(p * p, max_nums + 1, p):
                is_prime[i] = False
        p += 1
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if sum(is_prime[i] for i in range(1, n + 1)) % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    return "Maria" if maria_wins > ben_wins else "Ben"

