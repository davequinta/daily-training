'''
Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers
Returns

float: the resulting float value rounded to 3 places after the decimal
Input Format

The first line contains the integer, , the size of .
The second line contains the  space-separated integers, .

Constraints


Sample Input

STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output

169.375
Explanation

Here, set is the set containing the distinct heights. Using the sum() and len() functions, we can compute the average.





'''


def average(array):
    # your code goes here
    sHeights = set(array)
    result = sum(sHeights)/len(sHeights)
    return result


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
