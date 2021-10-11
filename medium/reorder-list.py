'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # we need to find the first and 2nd half of the list
        # 1 -> 2 -> 3 -> 4 -> 5
        # 2nd half would be 4->5
        # in this case slow would end up at 3 which is the first half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # the beginning of 2nd half of the list will be slow.next
        # in this case 3-> None and second will equal to 4
        second = slow.next
        prev = slow.next = None
        # now we reverse the 2nd half of the list 4->5 will be 5->4

        while second:
            tmp = second.next  # 1) tmp = 5,     2) tmp = Null
            second.next = prev  # 1) 4 -> Null,  2) 5 -> 4 in this example in 2nd iteration we have reversed it
            prev = second  # 1) prev = 4,        2) prev = 5
            second = tmp  # 1) second = 5,       2) second = Null

        # merge the 2 halfs
        # we need to find the beginning of the 2nd half
        # prev will be equal to the last node we looked at
        # and the prev will be the new head of 2nd half (5 in this case)
        # 1st half will have the original head
        first, second = head, prev

        # now we merge
        # the 2nd half can be shorter than the first so we do
        while second:
            # we need to store the next nodes in tmp variables because we will be breaking the links
            tmp1, tmp2 = first.next, second.next  # tmp1 = 2, tmp2 = 4   2) tmp1 = 3, tmp2 = null
            first.next = second  # 1 -> 5                                2) 2 -> 4
            second.next = tmp1  # 5 -> 2                                 2) 4 -> 3
            first = tmp1  # first = 2                                    2) first = 3
            second = tmp2  # second = 4                                  2) second = null... it ends here

            # so in our example we get 1 -> 5 -> 2 -> 4 -> 3
