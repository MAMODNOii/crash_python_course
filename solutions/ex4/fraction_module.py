"""
===============================================================================
			fraction_module
===============================================================================

This module contains all the functions used to convert an input rational number
to a simplified-form fraction in terms of its numerator and denominator.

"""

from ex3_module import prime_sieve_of_eratosthenes, prime_factors
import math

def simplified_fraction(numerator, denominator):
    """
    A function that reduces an input fraction (in the forms of numerator and denominator) 
    to its simplified form exploiting the pri,e decomposition of the numerator and denominator.


    Parameters
    ----------
    numerator : int
        the numerator of the input fraction
    denominator : int
        the denominator of the input fraction

    Returns
    -------
    (numerator, denominator) : tuble
        the simplified form of the fraction
    """
    prime_numerators = set(prime_factors(numerator,prime_sieve_of_eratosthenes(denominator)))
    prime_denominators = set(prime_factors(denominator,prime_sieve_of_eratosthenes(denominator)))

    prime_co = prime_numerators.intersection(prime_denominators)
    if len(prime_co) != 0:
        total = math.prod(prime_co)
        numerator /= total
        denominator /= total

    return (numerator, denominator)

def continued_fraction_approx(num, precision):
    """
    A function that approximate the input rational number (num) as a fraction using continued fractions 
    by returing the tuple of the numerator and denominator.
    (see more detail: https://en.wikipedia.org/wiki/Continued_fraction#Best_rational_approximations)

    Parameters
    ----------
    num : float
        the real number to approximate
   precision : float 
        the precision threshold to stop the iteration

    Returns
    -------
    (numerator, denominator) : tuble
        the best fraction approximation of num
    """

    # Check whether the input number is negative or positive
    # If negative, convert it to a positive and store the sign and at the end return the sign in its numerator
    if num < 0.: 
        sign = -1
        num = sign*num
    else: sign = 1

    # Implement continued fractions
    # 1.Initialisation of variables:
    a0 = math.floor(num)
    x1 = num - a0

    if abs(x1) < precision:
        return (a0, 1)

    numerators = [1, a0]
    denominators = [0, 1]

    while True:
        if x1 == 0:
            break

        a = math.floor(1 / x1)
        x1 = 1 / x1 - a

        numerators.append(a * numerators[-1] + numerators[-2])
        denominators.append(a * denominators[-1] + denominators[-2])

        approx = numerators[-1] / denominators[-1]
        if abs(approx - num) <= precision:
            break

    # Simplified fraction
    numerator, denominator = simplified_fraction(numerators[-1], denominators[-1])

    return (sign*numerator, denominator)
