'''
Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        first, last = head, head
        vals = []

        while last:
            vals.append(last.val)
            last = last.next

        print(vals)
        l, r = 0, len(vals) - 1
        while l < r:
            if vals[l] != vals[r]:
                return False
            l += 1
            r -= 1
        return True


class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # find the middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse 2nd half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # check plaindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


s = Solution2()
head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(s.isPalindrome(head))
