"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

And then read line by line: "PAHNAPLSIIGYIR"
"""

import time

class Solution(object):
    def convert(self, s, numRows):

        if numRows == 1:
            return s

        arr=list(range(numRows*2 - 2,-1,-2))
        arr2=list(range(0,numRows*2 - 1,2))

        arr = [[arr[i],arr2[i]] for i in range(len(arr))]

        s = list(s)

        ret = []

        counter = 1
        last_index = 0

        for i in range(numRows):
            pair = arr[i]

            while last_index < len(s):
                if pair[counter%2] != 0:
                    ret.append(s[last_index])
                    last_index += pair[counter%2]
                counter += 1
            
            last_index = i+1

            counter = 0

        return ''.join(ret)

"""

"""

def main():
    sol = Solution()

    # s = "PAYPALISHIRING"
    # n = 3
    # print(sol.convert(s,n))

    # s = "PAYPALISHIRING"
    # n = 4
    # print(sol.convert(s,n))

    s = "A"
    n = 1
    print(sol.convert(s,n))

    s = "PAYPALISHIRING"
    n = 7
    print(sol.convert(s,n))


if __name__ == '__main__':
    start = time.time()
    main()
    print("\n\nTotal process time: {:.20f} seg.".format(time.time()-start))

"""
P   A   H   N       P     I     N       P       H       P         R     P           N
A P L S I I G       A   L S   I G       A     S I       A       I I     A         I G
Y   I   R           Y A   H R           Y   I   R       Y     H   N     Y       R
                    P     I             P L     I G     P   S     G     P     I
                                        A       N       A I             A   H
                                                        L               L S
                                                                        I

Example 1:  Input: s = "PAYPALISHIRING",    numRows = 3     Output: "PAHNAPLSIIGYIR"    
Example 2:  Input: s = "PAYPALISHIRING",    numRows = 4     Output: "PINALSIGYAHRPI"
Example 3:  Input: s = "A",                 numRows = 1     Output: "A"

Algorithm:
if column = 3   if column = 4   if column = 5   if column = 6   if column = 7
4,0 letters     6,0 letters     8,0 letters     10,0 letters    12,0 letters
2,2 letters     4,2 letters     6,2 letters     8,2 letters     10,2 letters
0,4 letters     2,4 letters     4,4 letters     6,4 letters     8,4 letters
                0,6 letters     2,6 letters     4,6 letters     6,6 letters
                                0,8 letters     2,8 letters     4,8 letters
                                                0,10 letters    2,10 letters
                                                                0,12 letters


1) Hacer arrays de [n*2-2:0:-2] y [0:n*2-2:2]
2) Loop a traves del string siguiendo esos array de 1 a 1 (usar un contador i%2 para ver cual de los dos usar)

"""
