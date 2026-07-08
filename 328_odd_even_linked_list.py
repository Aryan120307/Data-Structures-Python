"""
LeetCode 328 - Odd Even Linked List
Difficulty: Medium
Topic: Linked List

Problem Link:
https://leetcode.com/problems/odd-even-linked-list/

====================================================
Approach 1: Extra Lists
Time Complexity: O(n)
Space Complexity: O(n)
====================================================

# Create two separate linked lists:
# 1. Odd position nodes
# 2. Even position nodes
# Connect both lists at the end.


====================================================
Approach 2: In-place Rearrangement (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:

            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
