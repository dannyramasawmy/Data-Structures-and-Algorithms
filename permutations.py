import math
import sys


def strPermute(s, myset, l=''):
    """
    Print permutations.
    """
    if len(s) == 0:
        print(l+'')
        myset.add(l+s)
    else:
        for idx, ll in enumerate(s):
            subs = s[0:idx] + s[idx+1:]
            strPermute(subs, myset, l+ll)

mystring = '1234'
myset = set()
strPermute(mystring, myset)


