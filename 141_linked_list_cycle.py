"""
LeetCode 141 - Linked List Cycle
Difficulty: Easy
Topic: Linked List

Problem Link:
https://leetcode.com/problems/linked-list-cycle/

====================================================
Approach 1: Hash Set
Time Complexity: O(n)
Space Complexity: O(n)
====================================================

class Solution:
    def hasCycle(self, head):

        visited = set()

        current = head

        while current:

            if current in visited:
                return True

            visited.add(current)
            current = current.next

        return False


====================================================
Approach 2: Floyd's Cycle Detection (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def hasCycle(self, head):

        slow = head
        fast = head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
