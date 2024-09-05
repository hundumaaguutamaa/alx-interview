#!/usr/bin/python3

def is_prime(n):
  """
  Efficiently checks if a number is prime using trial division up to the square root of n.
  """
  if n <= 1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def sieve_of_eratosthenes(n):
  """
  Generates a list of prime numbers up to a given limit n using the Sieve of Eratosthenes.
  """
  primes = [True] * (n + 1)
  primes[0] = primes[1] = False
  for i in range(2, int(n**0.5) + 1):
    if primes[i]:
      for j in range(i * i, n + 1, i):
        primes[j] = False
  return [i for i, is_prime in enumerate(primes) if is_prime]

def isWinner(x, nums):
  """
  Determines the winner of the game based on the number of rounds x and the set of numbers nums.
  """
  # Pre-calculate primes up to the maximum number in nums for faster lookups
  max_num = max(nums)
  primes = sieve_of_eratosthenes(max_num)
  
  # Track wins for Maria and Ben
  maria_wins = 0
  ben_wins = 0
  
  for _ in range(x):
    # Since Maria starts, check if there are any primes
    if not any(is_prime(num) for num in nums):
      ben_wins += 1
      continue
    
    # Remove multiples of the chosen prime for each round
    for prime in primes:
      if prime in nums:
        nums = [num for num in nums if num % prime != 0]
        break
  
    # Check who has no remaining moves (no primes)
    if not any(is_prime(num) for num in nums):
      maria_wins += 1

  # Return winner or None if tied
  if maria_wins > ben_wins:
    return "Maria"
  elif maria_wins < ben_wins:
    return "Ben"
  else:
    return None
