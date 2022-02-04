'''
Given the head of a linked list,
remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # time complexity: O(n)
        # space complexity: O(1)
        # we use a dummy node to make the head node easier to handle
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # move right pointer n steps ahead
        while n > 0 and right:
            right = right.next
            n -= 1

        # we keep moving till right is None
        while right:
            left = left.next
            right = right.next

        # delete the node
        left.next = left.next.next

        return dummy.next


s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.removeNthFromEnd(head, 2))
