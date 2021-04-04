"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
- Read in and ignore any leading whitespace.
- Check if the next character (if not already at the end of the string) is '-' or '+'. Assume the result is positive if neither is present.
- Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
- Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 

Example 1:  Input: s = "42"                 Output: 42
Example 2:  Input: s = "   -42"             Output: -42
Example 3:  Input: s = "4193 with words"    Output: 4193
Example 4:  Input: s = "words and 987"      Output: 0
Example 5:  Input: s = "-91283472332"       Output: -2147483648
"""

import time


class Solution(object):
    def myAtoi(self, x):
        INT32 = 2**31
        num_negativo = False
        first = -1
        last = 0
        found_first = False

        for i in range(len(x)):
            if " " == x[i]:
                if not found_first:
                    continue
                else:
                    break
            elif "-" == x[i]:
                if not found_first:
                    found_first = True
                    num_negativo = True
                    first = i
                    last = i
                    continue
                else:
                    break
            elif "+" == x[i]:
                if not found_first:
                    found_first = True
                    first = i
                    last = i
                    continue
                else:
                    break
            elif x[i].isdigit():
                found_first = True
                if first == -1:
                    first = i
                    last = i
                else:
                    last = i
            else:
                break

        if first != -1:
            try:
                if not num_negativo:
                    return min([int(x[first:last+1]),INT32-1])
                else:
                    return max([int(x[first:last+1]),-INT32])
            except:
                pass
        return 0


def main():
    sol = Solution()

    s = "42"
    print(sol.myAtoi(s))

    s = "   -42" 
    print(sol.myAtoi(s))

    s = "4193 with words"
    print(sol.myAtoi(s))

    s = "words and 987"
    print(sol.myAtoi(s))

    s = "-91283472332"
    print(sol.myAtoi(s))

    s = "-+12"
    print(sol.myAtoi(s))

    s = "+-234word5"
    print(sol.myAtoi(s))


if __name__ == '__main__':
    start = time.time()
    main()
    print("\nTotal process time: {:.20f} seg.".format(time.time()-start))