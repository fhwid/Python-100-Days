"""
check the username and QQ number
"""

import re


def main():
    username = input('Pls input the username:')
    qq = input('Pls input the QQ number:')
    # the first Arg of match is re expr
    # the second Arg is the string to be matched
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not m1:
        print('Pls input a valid username.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Pls input a valid QQ num.')
    if m1 and m2:
        print('your input is valid.')



if __name__ == "__main__":
    main()


