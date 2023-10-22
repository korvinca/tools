#!/bin/python3
"""
Task 
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-2
integer denoting the maximum number of consecutive 1's in n's binary representation. 
When working with different bases, it is common to show the base as a subscript.
"""
# import math
# import os
# import random
# import re
# import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        if ( n >= 6 ) or ( n <= 20 ):
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a // b)
    print(a / b)