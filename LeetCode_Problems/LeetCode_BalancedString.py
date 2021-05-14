"""
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
Return 0 if the string is already balanced.

Example 1:  Input: s = "QWER"   Output: 0   Explanation: s is already balanced.
Example 2:  Input: s = "QQWE"   Output: 1   Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:  Input: s = "QQQW"   Output: 2   Explanation: We can replace the first "QQ" to "ER". 
Example 4:  Input: s = "QQQQ"   Output: 3   Explanation: We can replace the last 3 'Q' to make s = "QWER".

Algoritmo: Search in letters the number of repetitions
"""
#import pytest
import time


class Solution(object):
    def balancedString(self, s):
        times = int(len(s)/4)
        letters = set(s)

        suma = 0
        for i in letters:
            count = s.count(i)
            if count > times:
                suma += (count - times)

        return suma

def main():
    pass


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nTotal process time: {:.20f} seg.".format(time.time()-start))