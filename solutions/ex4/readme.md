# Solution of Exercise 4

- I have created a new class **rational** to handle a new type of rational numbers, avalaible in [rational_class](rational_class.py).

- The class has been done with the aid of two additional modules [fraction_module](../fraction_module.py) and [ex3_module](ex_module.py).

- Finally, it is tested in the jupyter notebook [ex4_test](ex4_test.ipynb)


## rational class
Here, I will describe the constructors of this class:
* **``__init__``** 
  - take
    - a positional argument for the number to convert into a rational number
    - a keyword argument to set the required precision of the approximation, then check whether its value is in between 0 and 1. if not print an error message if the criterion is not reached.
  - store internally by using the function **continued_fraction_approx** in the module [fraction_module](fraction_module.py)
    - the numerator and denominator representing the rational number (``self.numerator`` and ``self.denominator``)
    - the sign of your rational number should be stored in the numerator
  
* **``__abs__``** to deal with their absolute values

* **String types** to deal with ``__str__`` and ``__repr__``.

* **Comparison operators** to deal with ``__eq__``, ``__ne__``, ``__lt__``, ``__gt__``, ``__le__``, and ``__ge__``.

* **``__int__`` and ``__float__``** to perform a casting of the rational number into integers and floats.


## Additional modules
There are two external modules used in this class:
* [fraction_module](fraction_module.py) contains functions used to convert an input rational number to a simplified-form fraction in terms of its numerator and denominator. There are two used functions:
  - **simplified_fraction** to reduce an input fraction (in the forms of numerator and denominator) to its simplified form exploiting the prime decomposition of the numerator and denominator;
  - **continued_fraction_approx** to approximate the input rational number as a fraction using continued fractions and return the tuple of its numerator and denominator.
* [ex3_module](ex_module.py) contains all the functions which are built in [exercise3_pythonbasics](../ex3) and will be used in [fraction_module](fraction_module.py). There are two used functions:
  - **prime_sieve_of_eratosthenes** to find the list of prime integer numbers less than or equal to the input number;
  - **prime_factors** to find the decomposition in prime factors of an input positive integer number.
  

## Test
I have done 7 tests of the class in [ex4_test](../ex4_test.ipynb):
* Check for the precision is in between 0 and 1, and print an error message if the criterion is not reached
* Test the fraction estimation of rational numbers and the sign stored in its numerator
* Test ``__str__`` and ``__repr__``
* Test ``__int__`` and ``__float__``
* Test ``__abs__``
* Test arithmetic dundler functions (e.g. ``__add__``, ``__mul__``, ...)
* Test comparison operators (e.g. ``__eq__``,``__gt__``, ...)

They have been tested using ``assert`` module. If the results from the class are different from the expected values (either computed by python or by hands), the error messages will be printed out.
