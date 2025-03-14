#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: ex3.4_solution.py

def prime_sieve_of_eratosthenes(max_num):
    """A function that finds the list of prime integer numbers less than or equal to the maximum number (max_num)
       , starting by knowing that 2 is a prime number and using Sieve of Eratosthenes algorithm
       (see more detail: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

    Parameters
    ----------
    max_num : int 
        the maximum number which is possible to be in the output list of prime integer numbers

    Returns
    -------
    : list
        a list with the prime integer numbers
    """
    
    # Crete a Boolean mask to indicate which numbers are prime 
    primes = [True] * (max_num + 1)  # Initially assume all numbers (from 0 to n) are prime
    primes[0] = primes[1] = False  # Set 0 and 1 are not prime, and 2 is the smallest prime number
    
    # Modify the Boolean mask using Sieve of Eratosthenes algorithm
    for num in range(2, int(max_num ** 0.5) + 1):
        if primes[num]:  # If num is prime
        # Start enumerating the multiples of each prime (num) from num**2 to max_num
            for multiple in range(num * num, max_num + 1, num):
                primes[multiple] = False  # Mark multiples as non-prime
    
    # Create the list of the prime integer numbers using the final Boolean mask
    prime_numbers = [num for num in range(max_num+1) if primes[num]]
    
    return prime_numbers


if __name__ == "__main__":
    
    prime_numbers = prime_sieve_of_eratosthenes(100)
    print(prime_numbers)
