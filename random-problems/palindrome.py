import string


def isPalindrome(x):
    x = x.replace(' ', '').translate(
        str.maketrans('', '', string.punctuation)).lower()
    print(x)
    return x == x[::-1]


if __name__ == '__main__':
    print(isPalindrome("Go hang a salami, I'm a lasagna hog."))
