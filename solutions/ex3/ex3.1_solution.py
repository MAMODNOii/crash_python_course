#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# File: ex3.1_solution.py

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
        
if __name__ == "__main__":
    print("# Check whether the input number is divisible by 2, 3, 5, or 7")
    
    num = int(input("Enter an integer: "))
    check_divisibility(num)
    print()
    
    print("# Check whether the first input number is divisible by the other one (and vice-versa)")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divisible_bw_2nums(num1, num2)
