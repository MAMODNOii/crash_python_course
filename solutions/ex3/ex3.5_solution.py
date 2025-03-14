#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: ex3.5_solution.py

import ex3_module
        
def _test_prime_factors():
    """
    Tests the prime_factors function for all numbers from 1 to 100.
    """
    
    print("# Tests the prime_factors function for all numbers from 1 to 100.")
    for num in range(1,101):
        prime_numbers = ex3_module.prime_sieve_of_eratosthenes(num)
        prime_factors_arr = ex3_module.prime_factors(num, prime_numbers)
        print(f'For {num}: the decomposition in prime factors is', prime_factors_arr)

if __name__ == "__main__":
    _test_prime_factors()

