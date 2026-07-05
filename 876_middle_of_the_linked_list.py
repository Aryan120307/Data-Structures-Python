"""
LeetCode 876 - Middle of the Linked List
Difficulty: Easy
Topic: Linked List

Problem Link:
https://leetcode.com/problems/middle-of-the-linked-list/

====================================================
Approach 1: Count Length
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

# Count the total number of nodes.
# Traverse again to reach the middle node.

class Solution:
    def middleNode(self, head):

        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        middle = length // 2
        current = head

        while middle:
            current = current.next
            middle -= 1

        return current


====================================================
Approach 2: Fast & Slow Pointer (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def middleNode(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
