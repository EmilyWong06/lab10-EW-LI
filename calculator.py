"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    math.sqrt(a)
    if a < 0:
        raise ValueError # square root

def hypotenuse(a, b):
    math.hypot(a, b) # hypotenuse

def add(a, b): 
    return a + b

def subt(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError # value error
    if b <= 0:
        raise ValueError # value error
    return math.log(b, a)

def exp(a, b):
    return a ** b