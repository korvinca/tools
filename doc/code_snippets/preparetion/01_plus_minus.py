#!/bin/python3
'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.
Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
Example 

There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
0.400000
0.400000
0.200000
'''


import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total_elements = len(arr)
    positive_count = sum(1 for num in arr if num > 0)
    negative_count = sum(1 for num in arr if num < 0)
    zero_count = total_elements - positive_count - negative_count

    positive_ratio = positive_count / total_elements
    negative_ratio = negative_count / total_elements
    zero_ratio = zero_count / total_elements

    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    # n = int(input().strip())
    # arr = list(map(int, input().rstrip().split()))

    n = 5
    arr = [0, 0, -1, 1, 1]
    plusMinus(arr)