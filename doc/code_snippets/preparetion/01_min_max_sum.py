#Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0
    arr.sort()  # Sort the array in ascending order
    min_sum = sum(arr[:-1])  # Sum of the first four integers (excluding the maximum)
    max_sum = sum(arr[1:])   # Sum of the last four integers (excluding the minimum)
    print(min_sum, max_sum)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)