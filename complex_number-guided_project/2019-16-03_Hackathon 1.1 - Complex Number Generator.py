#Team 3::: Complex Number Challenge

#%%
##Importing classes
import os
from datetime import datetime as dt
import random as rd
import math as mt
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pyplt
import seaborn as sb

#Code starts here
#%%
##Defining a class `complex_numbers` that accepts two parameters
class Complex_Numbers:
    "This is a complex-number calculator that allows basic operations on complex numbers. Note: syntax is 'a + bi'"
    info = "I allow you to do some basic math with complex numbers. Note: syntax is 'a + bi'."
    ##Importing the usually necessary libraries
    import os
    from datetime import datetime as dt
    import random as rd
    import math as mt
    import numpy as np
    import pandas as pd
    import matplotlib as plt
    import matplotlib.pyplot as pyplt
    import seaborn as sb
    ##Initiating the class with a self object comprising two variables, the first is real and teh second is imaginary
    def __init__(self, real, imag):
        ##Setting Type Errors for incorrectly entered values
        if type(real) != int and type(real) != float:
            raise TypeError("PLEASE ENTER PROPER NUMERIC VALUES.")
        elif type(imag) != int and type(imag) != float:
            raise TypeError("PLEASE ENTER PROPER NUMERIC VALUES.")
        else:
            self.real = real
            self.imag = imag
    ##Defining a function to output the complex number as is the norm, using the two variables of the created object
    def __repr__(self):
        "Outputs the complex number from the numerals you have entered."
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        elif self.real == 0:
            return "%.2fi" % self.imag
        elif self.imag == 0:
            return "%.2f" % self.real
        else:
            return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
        print()
    ##Defining a function that sums two complex numbers
    def __add__(self, other):
        "Outputs the sum of two complex numbers."
        ##Passing the summed values as a new object of the class "Complex_NUmbers"
        sum_comp = Complex_Numbers(self.real + other.real, self.imag + other.imag)
        ##Calling out the earlier defined function that outputs the complex number as is the norm, using the two variables of the created object
        return sum_comp.__repr__()
    ##Defining a function that substracts two complex numbers
    def __sub__(self, other):
        "Outputs the difference between the first and second complex numbers."
        ##Passing the substracted values as a new object of the class "Complex_NUmbers"
        diff_comp = Complex_Numbers(self.real - other.real, self.imag - other.imag)
        ##Calling out the earlier defined function that outputs the complex number as is the norm, using the two variables of the created object
        return diff_comp.__repr__()
    ##Defining a function that multiplies two complex numbers
    def __mul__(self, other):
        "Outputs the product of two complex numbers."
        ##Creating two new variables to make for easy code: these capture the product values
        prod_real = (self.real*other.real) - (self.imag*other.imag)
        prod_imag = (self.real*other.imag) + (self.imag*other.real)
        ##Passing the above variables as a new object of the class "Complex_NUmbers"
        prod_comp = Complex_Numbers(prod_real, prod_imag)
        ##Calling out the earlier defined function that outputs the complex number as is the norm, using the two variables of the created object
        return prod_comp.__repr__()
    ##Defining a function that divides two complex numbers
    def __truediv__(self, other):
        "Outputs the division of the first complex number with the second."
        ##Creating two new variables to make for easy code: these capture the division values
        tdiv_real = ((self.real*other.real) + (self.imag*other.imag))/(other.real**2 + other.imag**2)
        tdiv_imag = ((self.imag*other.real) - (self.real*other.imag))/(other.real**2 + other.imag**2)
        ##Passing the above variables as a new object of the class "Complex_NUmbers"
        tdiv_comp = Complex_Numbers(tdiv_real, tdiv_imag)
        ##Calling out the earlier defined function that outputs the complex number as is the norm, using the two variables of the created object
        return tdiv_comp.__repr__()
    ##Defining a function that gives the absolute value of a complex number
    def absolute(self):
        "Outputs the absolute value of a complex number."
        ##Saving the output as a variable in case it is needed ever
        abs_comp = mt.sqrt(self.real**2 + self.imag**2)
        return abs_comp
    def argument(self):
        "Outputs the argument (in Radians) of a complex number; i.e., arctan of the real and imaginary parts."
        ##Saving the output as a variable in case it is needed ever; note the use of the np.arctan function
        arg_comp = np.arctan([self.real, self.imag])
        return arg_comp
    def conjugate(self):
        "Outputs the conjugate of a complex number; i.e., 'a - bi' if the number is 'a + bi'."
        ##Saving the output as a variable in case it is needed ever
        conj_comp = Complex_Numbers(self.real, -1*self.imag)
        return conj_comp.__repr__()

#%%
##Defining two objects as instructed
comp_1 = Complex_Numbers(3, 5)
comp_2 = Complex_Numbers(4, 4)

#%%
##Creating variables to store the various operations
comp_sum = comp_1.__add__(comp_2)
comp_diff = comp_1.__sub__(comp_2)
comp_prod = comp_1.__mul__(comp_2)
comp_quot = comp_1.__truediv__(comp_2)
comp_abs = comp_1.absolute()
comp_arg = comp_1.argument()
comp_conj = comp_1.conjugate()

#Code ends here