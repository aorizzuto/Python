"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:  Input: nums1 = [1,3], nums2 = [2]   Output: 2.00000     Explanation: merged array = [1,2,3] and median is 2.
Example 2:  Input: nums1 = [1,2], nums2 = [3,4] Output: 2.50000     Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:  Input: nums1 = [0,0], nums2 = [0,0] Output: 0.00000     
Example 4:  Input: nums1 = [], nums2 = [1]      Output: 1.00000
Example 5:  Input: nums1 = [2], nums2 = []      Output: 2.00000
"""

import time

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1+nums2)
        n = len(arr)

        if n != 0:
            if n%2 == 1:
                return arr[int(n/2)]
            else:
                n=int(n/2)
                return float(arr[n]+arr[n-1])/2
        return 0

        


def main():
    sol = Solution()

    nums1 = [1,3]
    nums2 = [2]
    print(sol.findMedianSortedArrays(nums1,nums2))

    nums1 = [1,2]
    nums2 = [3,4]
    print(sol.findMedianSortedArrays(nums1,nums2))

    nums1 = [0,0]
    nums2 = [0,0]
    print(sol.findMedianSortedArrays(nums1,nums2))

    nums1 = []
    nums2 = [1]
    print(sol.findMedianSortedArrays(nums1,nums2))

    nums1 = [2]
    nums2 = []
    print(sol.findMedianSortedArrays(nums1,nums2))




if __name__ == '__main__':
    start = time.time()
    main()
    print("\n\nTotal process time: {:.20f} seg.".format(time.time()-start))