"""
=======================================================================================================
			rational_class
=======================================================================================================

This class is built to deal with rational numbers by
- convert approximately them to fractions and restore them in the forms of numerator and denominator;
- deal with their absolute values
- deal with their string types
- deal with the casting of rational numbers into integers and floats
- deal with the arithmetic dundler functions between them
- deal with the comparison operators between them

"""

from fraction_module import simplified_fraction, continued_fraction_approx

class rational():
    """This class is used to handle rational numbers
    """
    
    def __init__(self, num, precision=1.e-5):
        
        # Check precision is in between 0 and 1 if not, print an error message 
        if not (0 <= precision <= 1):
            raise ValueError("Precision must be between 0 and 1.")
            
        self.num = num
        self.precision = precision
        self.numerator, self.denominator = continued_fraction_approx(self.num,self.precision)            
    
    def __abs__(self):
        return abs(self.numerator) / self.denominator
    
    def __str__(self):
        return f'{self.numerator}/{self.denominator}'
    
    def __repr__(self):
        return f'{type(self).__name__}({self.num}, precision={self.precision})'
    
    def __int__(self):
        return int(self.numerator / self.denominator)
    
    def __float__(self):
        return self.numerator / self.denominator
    
    # Overload all the arithmetic operators
    def __add__(self, other):
        up = self.numerator * other.denominator + other.numerator * self.denominator
        down = self.denominator * other.denominator
        return type(self)(up / down)
    
    def __sub__(self, other):
        up = self.numerator * other.denominator - other.numerator * self.denominator
        down = self.denominator * other.denominator
        return type(self)(up / down)
    
    def __mul__(self, other):
        up = self.numerator * other.numerator
        down = self.denominator * other.denominator
        return type(self)(up / down)
    
    def __truediv__(self,other):
        up = self.numerator * other.denominator
        down = self.denominator * other.numerator
        return type(self)(up / down)
    
    def __pow__(self, exponent):
        return type(self)((self.numerator ** exponent) / (self.denominator ** exponent))
    
    # Overload all the comparison operators
    def __eq__(self, other):
        return (self.numerator,self.denominator) == (other.numerator,other.denominator)
    
    def __ne__(self, other):
        return (self.numerator,self.denominator) != (other.numerator,other.denominator)
    
    # Note that I compare 2 fractions using cross multiplication
    
    def __lt__(self, other): # <
        return self.numerator * other.denominator < other.numerator * self.denominator
    
    def __gt__(self, other): # >
        return self.numerator * other.denominator > other.numerator * self.denominator
    
    def __le__(self, other): # <=
        return self.numerator * other.denominator <= other.numerator * self.denominator
    
    def __ge__(self, other): # >=
        return self.numerator * other.denominator >= other.numerator * self.denominator
