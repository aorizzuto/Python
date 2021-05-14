"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:  Input: x = 123  Output: 321
Example 2:  Input: x = -123 Output: -321
Example 3:  Input: x = 120  Output: 21
Example 4:  Input: x = 0    Output: 0
"""

import time

# abs(n) <= 0xffffffff

INT32 = 2**31

class Solution(object):
    def reverse(self, x):
        
        if x >= 0:
            ret = int(str(x)[::-1])
        else:
            ret = int(str(x)[:0:-1])*(-1)

        if -INT32 < ret < (INT32-1):
            return ret

        return 0


def main():
    sol = Solution()

    x = 123
    print(sol.reverse(x))

    x = -123
    print(sol.reverse(x))

    x = 120
    print(sol.reverse(x))

    x = 0
    print(sol.reverse(x))


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nTotal process time: {:.20f} seg.".format(time.time()-start))