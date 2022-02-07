'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
'''

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity: O(nlogk)
        # space complexity: O(1)

        if not lists or len(lists) == 0:
            return None

        # We will take pairs of linked lists and merging them each time
        # keep doing this till there is only one linked list remaining
        while len(lists) > 1:
            merged_list = []

            # we need to do pairs so we inc by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                # l2 could be out of bounds so care for that
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.mergeList(l1, l2))
            lists = merged_list
        # return the last remaining linked list
        return lists[0]

    # this is leetcode's merge two sorted lists (easy) problem at this point
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        return dummy.next


s = Solution()
