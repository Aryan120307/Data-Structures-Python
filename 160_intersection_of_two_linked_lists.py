"""
LeetCode 160 - Intersection of Two Linked Lists
Difficulty: Easy
Topic: Linked List

Problem Link:
https://leetcode.com/problems/intersection-of-two-linked-lists/

====================================================
Approach 1: Hash Set
Time Complexity: O(m + n)
Space Complexity: O(m)
====================================================

class Solution:
    def getIntersectionNode(self, headA, headB):

        visited = set()

        current = headA

        while current:
            visited.add(current)
            current = current.next

        current = headB

        while current:
            if current in visited:
                return current
            current = current.next

        return None


====================================================
Approach 2: Two Pointer Switching (Optimal)
Time Complexity: O(m + n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def getIntersectionNode(self, headA, headB):

        if not headA or not headB:
            return None

        currA = headA
        currB = headB

        while currA != currB:

            currA = currA.next if currA else headB
            currB = currB.next if currB else headA

        return currA
