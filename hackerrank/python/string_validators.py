'''
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
str.isdigit()
This method checks if all the characters of a string are digits (0-9).

>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).

>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
Task

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
Language
Python 3

More
12345678
if __name__ == '__main__':
    s = input()
    #Ternary  <expression 1> if <condition> else <expression 2> 
    print(any(a.isalnum() for a in s) )
    print(any(a.isalpha() for a in s) )
    print(any(a.isdigit() for a in s) )
    print(any(a.islower() for a in s) )
    print(any(a.isupper() for a in s) )
Line: 1 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
Congratulations!

You have passed the sample test cases. Click the submit button to run your code against all the test cases.


Sample Test case 0
Input (stdin)

Download
qA2
Your Output (stdout)
True
True
True
True
True
Expected Output

Download
True
True
True
True
True

Reference: https://www.programiz.com/python-programming/methods/built-in/any

'''
if __name__ == '__main__':
    s = input()
    print(any(a.isalnum() for a in s))
    print(any(a.isalpha() for a in s))
    print(any(a.isdigit() for a in s))
    print(any(a.islower() for a in s))
    print(any(a.isupper() for a in s))
