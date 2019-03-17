#Team 3::: Python Mini Challenges

#%%
##Importing classes
import os
from datetime import datetime as dt
from collections import Counter
import random as rd
import math as mt
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as pyplt
import seaborn as sb


#%%
#PROBLEM 1:
##Defining a function that outs the lowest Palindrome number greater than the inputed number
def palindrome(num):
    "Outputs the lowest Palindrome number greater than the inputed number."
    ##Creating an exception error to handle non-int and non-float values
    if type(num) != int and type(num) != float:
        return TypeError("PLEASE ENTER A PROPER NUMERAL.")
    ##Creating an exception error to handle non-positive values
    elif num < 0:
        return ValueError("PLEASE ENTER A POSITIVE NUMBER.")
    else:
        ##Creating string and integer variables that will help us compute the Palindrome
        numint = int(num)
        strval = str(numint)
        strlen = len(strval)
        strmid = int(strlen/2)
        ##Checking if the integer value of the entered numeral is less than 9:
        ###if so, 1 is added to the integer value of the entered numeral and is outputted
        if numint <= 8:
            return numint + 1
        ##Checking if the integer value of the entered numeral is more than 8 and less than 11:
        ###if so, outputting 11
        elif numint < 11:
            return 11
        ##Checking if the integer value of the entered numeral is more than 10 and less than 99:
        ###if so, the lowest multiple of 11 greater than the integer value of the entered numeral is outputted       
        elif numint < 99:
            return 11*(numint//11 + 1)
        ##Checking if the integer value of the entered numeral is 99:
        ###if so, outputting 101
        elif numint == 99:
            return 101
        ##Checking if the integer value of the entered numeral is less than 999:
        ###if so, we set an if-elif-else loop that takes care of three possible contingencies:     
        elif numint < 999:
            ##Checking if the hundredth value is higher than the unit value:
            ###if so, we replace the unit value with the hundredth value, keeping everything else the same
            if int(strval[0]) > int(strval[2]):
                return int(strval[0] + strval[1] + strval[0])
            ##Checking if the tenth value is 9:
            ###if so, we add 1 to the hundreth value, keep the tenth value as 0, and replace the unit value with the sum of 1 and the hundreth value  
            elif int(strval[1]) == 9:
                return int(str(int(strval[0]) + 1) + "0" + str(int(strval[0]) + 1))
            ##Otherwise, we add 1 to the tenth value, and use the hundredth value for the both the hundredth and unit values
            else:
                return int(strval[0] + str(int(strval[1]) + 1) + strval[0])
        ##Checking if the integer value of the entered numeral is 1 less than any power of 10:
        ###if so, we simply output the sum of 2 and the integer value of the entered numeral
        elif 10**(strlen) - 1 == numint:
            return numint + 2
        ##Checking if the integer value of the entered numeral has even digits:
        ###if so, we set an if-else loop that takes care of two possible contingencies: 
        elif strlen%2 == 0:
            ##Creating left (left-half), reverse-left, and right (right-half) slices of the string of the integer value of the entered numeral;
            ###these will help us compute the Palindrome
            strval_left = strval[ : strmid]
            strval_leftrev = strval_left[ : : -1]
            strval_right = strval[strmid : ]
            ##Checking if the integer value of the reverse-left string is higher than that of the right string:
            ###if so, outputting the integer value of the concate of the left and reverse-left strings
            if int(strval_leftrev) > int(strval_right):
                return int(strval_left + strval_leftrev)
            ##Otherwise, adding 1 to the integer value of the left string, and computing the reverse-left string of the new left string;
            ###outputting the integer value of the concate of the new left and new reverse-left strings
            else:
                strval_left = str(int(strval_left) + 1)
                strval_leftrev = strval_left[ : : -1]
                return int(strval_left + strval_leftrev)
        ##Otherwise, we set an if-else loop that takes care of two possible contingencies:
        else:
            ##Creating left (effectively, from left to one value less than the middle), reverse-left, and right (effectively, from one value more than the middle to the right) slices of the string of the integer value of the entered numeral;
            ###these will help us compute the Palindrome            
            strval_left = strval[ : strmid]
            strval_leftrev = strval_left[ : : -1]
            strval_right = strval[strmid + 1 : ]
            ##Checking if the integer value of the reverse-left string is higher than that of the right string:
            ###if so, outputting the integer value of the concate of the left string, the middle value, and the reverse-left string
            if int(strval_leftrev) > int(strval_right):
                return int(strval_left + strval[strmid] + strval_leftrev)
            ##Otherwise, re-computing the left string to include the middle value, and adding 1 to the integer value of this new string, and computing the left-reverse string;
            ###outputting the integer value of the concate of the new left and new reverse-left strings
            else:
                strval_left = strval[ : strmid + 1]
                strval_left = str(int(strval_left) + 1)
                strval_leftrev = strval_left[ : : -1]
                return int(strval_left + strval_leftrev[1 : ])
#%%
##Checking the above function
print(palindrome("42"))
print(palindrome(-2))
print(palindrome(10.65))
print(palindrome(124))
print(palindrome(99999))
print(palindrome(23458482215485213185559876543098765439876543518155))


#%%
#PROBLEM 2:
##Defining a function that checks if the characters of the first string can be scrambled to putput the second string
def a_scramble(str_1, str_2):
    ##Importing the "Counter" function from the class collections
    from collections import Counter
    ##Saving the alphabet-wise counts of the two strings as variables:
    ###note that the Counter function outputs a dictionary
    letters = Counter(str_1.lower())
    word = Counter(str_2.lower())
    ##Checking if the Counter variable of the second string is a subset of the first, and outputting the same
    diff = word - letters
    return len(diff) == 0
#%%
##Checking the above function
print(a_scramble("Tom Marvolo Riddle","Voldemort"))
print(a_scramble("ticket","chat"))


#%%
#PROBLEM 3:
##Defining a function to check if a given number is a Fibonacci number
###We first define a sub-function to check if a number is a perfect square (i.e., square of two integers)
####We then check whether 5*(n^2) + 4 or 5*(n^2) - 4 is a perfect square: this is the mathematical check to assess if n is a Fibonacci number
def isFibonacci(n):
    def isPerfectSquare(x):
        from math import sqrt
        s = int(sqrt(x))
        return s*s == x
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
#%%
##Checking the above function
print(isFibonacci(12))
print(isFibonacci(377))


#%%
#PROBLEM 4:
##Defining a function that returns the string with it's letters and their occurrances continously together
def compress(word):
    ##Importing the "Counter" function from the class "collections"
    from collections import Counter
    ##Saving the Counter dictionary as a variable, starting an iterate with 0, and an empty string
    countdict = Counter(word.lower())
    stringout = ""
    i = 0
    ##Initiating a while loop to capture the characters from the keys and values of the above dictionary
    while i < len(countdict):
        stringout += str(list(countdict.keys())[i]) + str(list(countdict.values())[i])
        i += 1
    return stringout
#%%
##Checking the above function
print(compress("Bombay"))


#%%
#PROBLEM 5:
##Defining a function that given a string and number, checks whether the string's distinct characters amount to the entered number
def k_distinct(string, k):
    ##Importing the "Counter" function from the class "collections"
    from collections import Counter
    ##Saving the Counter dictionary as a variable, and comparing the length of the said dictionary with the entered numeral
    countdict = Counter(string.lower())
    return len(countdict) == k
#%%
##Checking the above function
print(k_distinct("Bombay", 5))
print(k_distinct("Poona", 5))