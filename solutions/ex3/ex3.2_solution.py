#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""File: ex3.2_solution.py
"""

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

def _test1():
    """Test case 1: Fibonacci sequence for even index elements"""
    fib_seq = fibonacci(n)
    even_index_list = [fib_seq[i] for i in range(len(fib_seq)) if i % 2 == 0]
    print("Test 1 - Even index elements:", even_index_list)

def _test2():
    """Test case 2: Fibonacci sequence for odd index elements"""
    fib_seq = fibonacci(n)
    odd_index_list = [fib_seq[i] for i in range(len(fib_seq)) if i % 2 != 0]
    print("Test 2 - Odd index elements:", odd_index_list)

if __name__ == '__main__':
    print("# Print the Fibonacci sequence up to the n-th term")
    n = int(input("Enter the number of terms (n): "))
    fib_list = fibonacci(n)
    print("Fibonacci sequence:", fib_list)
    print()
    
    _test1()
    _test2()
