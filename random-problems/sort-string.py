'''
Challenge: Write a Python Function to sort the words in a string alphabetically.

Input:
String of words separated by spaces

Output:
String of words, sorted alphabetically
'''


def sortWords(x):
    x = x.split(' ')
    return ' '.join(sorted(x, key=str.casefold))


if __name__ == '__main__':
    print(sortWords("banana ORANGE apple"))
