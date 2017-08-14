# MIT 6.00 - Introduction to Computer Science and Programming
# Problem Set 1
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00-introduction-to-computer-science-and-programming-fall-2008/assignments/pset1a.pdf
# Name: Tyler Furby
from StringIO import StringIO
from math import sqrt
import sys
import io

def findPrime():
    count = 1
    i = 1
    while count < 1000:
        i += 2
        for j in range(2, 1 + int(sqrt(i + 1))):
            if (i % j == 0):
                break
        else:
            count += 1
    print i

findPrime()
