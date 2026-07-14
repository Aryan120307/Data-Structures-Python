"""
LeetCode 2 - Add Two Numbers
Difficulty: Medium
Topic: Linked List

Problem Link:
https://leetcode.com/problems/add-two-numbers/

====================================================
Approach 1: Convert to Numbers
Time Complexity: O(n + m)
Space Complexity: O(n + m)
====================================================

# Convert both linked lists into integers.
# Add the integers.
# Convert the result back into a linked list.


====================================================
Approach 2: Digit-by-Digit Addition (Optimal)
Time Complexity: O(max(n, m))
Space Complexity: O(max(n, m))
====================================================
"""

class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)
            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
