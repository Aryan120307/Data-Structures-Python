"""
LeetCode 19 - Remove Nth Node From End of List
Difficulty: Medium
Topic: Linked List

Problem Link:
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

====================================================
Approach 1: Two-Pass (Length Counting)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def removeNthFromEnd(self, head, n):

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        if length == n:
            return head.next

        current = head
        steps = length - n

        for _ in range(steps - 1):
            current = current.next

        current.next = current.next.next

        return head


====================================================
Approach 2: One-Pass Fast & Slow Pointer (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # Delete the target node
        slow.next = slow.next.next

        return dummy.next
