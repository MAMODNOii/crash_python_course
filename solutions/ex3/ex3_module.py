#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: ex3_module.py that will be used in ex3.5_solution.py And also includes all functions have been built in the exercise 3


# Step 1: write the list of prime numbers which are smaller than or equal to the input number
# the same function as ex3.4
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


# Step 2: check if the number is divisible by the prime numbers in the list -> return the list of prime decomposition
def prime_factors(num, prime_numbers):
    """
    A function that finds the decomposition in prime factors of an input positive integer number
    
    Parameters
    ----------
    num : int 
        the integer number to find its decomposition in prime factors
    prime_numbers : list
        the list of prime numbers less than or equal
        
    Returns
    -------
    : list
        a list with the divisible prime numbers i.e. prime decomposition
    """    
    
    prime_factors = []
    
    for prime in prime_numbers:
        while num % prime == 0:
            prime_factors.append(prime)
            num //= prime

    return prime_factors
    


# ---------------------- Other functions in ex3 -------------------------------------------------

### ex3.1
def check_divisibility(number):
    """A function that reads an integer given as input from the user and 
    determines whether it is divisible by 2, 3, 5, or 7.

    Parameters
    ----------
    number : int 
        the input number to check its divisibility
        
    Returns
    -------
    : list
        the list of the divisible numbers of the input number
    """
    
    divisors = [2, 3, 5, 7]
    divisible_by = [d for d in divisors if number % d == 0]
        
    if divisible_by:
        print(f"{number} is divisible by {', '.join(map(str, divisible_by))}.")
    else:
        print(f"{number} is not divisible by 2, 3, 5, or 7.")
        
    return divisible_by 

def divisible_bw_2nums(num1, num2):
    """
    Checks if num1 is divisible by num2 and vice versa.
    
    Parameters
    ----------
    num1 : int 
        the integer number 1 to check if it is divisible by num2
    num2 : int 
        the another integer number 2 to check if it is divisible by num1
        
    Returns
    -------
    None: 
        prints the divisibility results.
    """
    
    if num2 != 0 and num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}.")
    else:
        print(f"{num1} is not divisible by {num2}.")
    
    if num1 != 0 and num2 % num1 == 0:
        print(f"{num2} is divisible by {num1}.")
    else:
        print(f"{num2} is not divisible by {num1}.")
        
### ex3.2
def fibonacci(n):
    """A function that calculates the Fibonacci sequence up to the n-th term

    Parameters
    ----------
    n : int 
        the n-th term of the sequence

    Returns
    -------
    : list
        a list with the Fibonacci sequence
    """
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    ret_list = [0, 1]
    for i in range(2, n):
        ret_list.append(ret_list[-1] + ret_list[-2])
    
    return ret_list

