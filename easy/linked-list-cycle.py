'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

3->2->0->4->2

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:

1->2->1

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:

1

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = head
        turtle = head
        # we move the turtle one step at a time but hare 2 steps
        # if its a cycle the turtle and hare will eventually equal eachother
        while head and hare and hare.next:
            hare = hare.next.next
            head = head.next
            if hare == head:
                return True

        return False
