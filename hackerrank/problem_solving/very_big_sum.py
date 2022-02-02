'''
In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in mind that some of those integers may be quite large.

Function Description

Complete the aVeryBigSum function in the editor below. It must return the sum of all array elements.

aVeryBigSum has the following parameter(s):

int ar[n]: an array of integers .
Return

long: the sum of all array elements
Input Format

The first line of the input consists of an integer .
The next line contains  space-separated integers contained in the array.

Output Format

Return the integer sum of the elements in the array.

Constraints


Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015
Note:

The range of the 32-bit integer is .
When we add several integer values, the resulting sum might exceed the above range. You might need to use long int C/C++/Java to store such sums.

Language
Python 3

More
1234567891011121314151617181920212223242526272829303132
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)

if __name__ == '__main__':

Line: 18 Col: 18

Submit Code

Run Code

Upload Code as File

Test against custom input
Problem Solving
You have earned 10.00 points!
You are now 59 points away from the 2nd star for your problem solving badge.
16%41/100
Congratulations
Share on FacebookShare on TwitterShare on LinkedIn
You solved this challenge. Would you like to challenge your friends?
Next Challenge
Earn a certificate in Problem Solving
Kudos on your progress! Take the HackerRank Skills Certification test and enrich your profile

Get Certified

Test case 0

Test case 1
Compiler Message
Success
Input (stdin)

Download
5
1000000001 1000000002 1000000003 1000000004 1000000005
Expected Output

Download
5000000015
Contest CalendarBlogScoring'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#


def aVeryBigSum(ar):
    # Write your code here
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
