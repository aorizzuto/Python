"""
You are given two non-empty linked lists representing two non-negative integers.

The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

import time

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l_1 = []
        l_2 = []

        l_1.append(l1.val)
        l_2.append(l2.val)

        nxt = l1.next
        nxt2 = l2.next

        while(nxt != None):
            l_1.append(nxt.val)
            nxt = nxt.next
        
        while(nxt2 != None):
            l_2.append(nxt2.val)
            nxt2 = nxt2.next

        lst1= ''.join([str(i) for i in l_1[::-1]])
        lst2= ''.join([str(i) for i in l_2[::-1]])
        s = str(int(lst1)+int(lst2))

        last = ListNode(val=int(s[0]))

        for i in range(len(s)-1):
            last = ListNode(val=int(s[i+1]), next = last)
          
        return last


def main():
    l1_3 = ListNode(3)
    l1_4 = ListNode(4,l1_3)
    l1_2 = ListNode(2,l1_4)

    l2_4 = ListNode(4)
    l2_6 = ListNode(6,l2_4)
    l2_5 = ListNode(5,l2_6)


    sol = Solution()

    print(sol.addTwoNumbers(l1_2,l2_5))

    l1 = ListNode(0)
    l2 = ListNode(0)

    print(sol.addTwoNumbers(l1,l2))




if __name__ == '__main__':
    start = time.time()
    main()
    print("\n\nTotal process time: {:.20f} seg.".format(time.time()-start))