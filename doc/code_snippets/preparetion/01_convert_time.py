#!/bin/python3
#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example
# Return '12:01:00'.
# Return '00:01:00'.

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    res = ""
    time_arr = s.split(":")
    if "PM" in s:
        if int(time_arr[0]) <= 11:
            new_time = int(time_arr[0]) + 12
            time_arr[0] = str(new_time)
            for i in time_arr:
                res += str(i)
                res += ":"
            res = res[:-3]
        else:
            res = s[:-2]
    else:
        if int(time_arr[0]) == 12:
            time_arr[0] = "00"
            for i in time_arr:
                res += str(i)
                res += ":"
            res = res[:-3]
        else:
            res = s[:-2]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
