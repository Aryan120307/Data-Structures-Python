"""
LeetCode 148 - Sort List
Difficulty: Medium
Topic: Linked List

Problem Link:
https://leetcode.com/problems/sort-list/

====================================================
Approach 1: Convert to Array + Sort
Time Complexity: O(n log n)
Space Complexity: O(n)
====================================================

# Store all node values in an array.
# Sort the array.
# Write the sorted values back into the linked list.


====================================================
Approach 2: Merge Sort on Linked List (Optimal)
Time Complexity: O(n log n)
Space Complexity: O(log n) (Recursion Stack)
====================================================
"""

class Solution:
    def sortList(self, head):

        if not head or not head.next:
            return head

        # Find middle node
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Merge sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):

        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:

            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        tail.next = l1 if l1 else l2

        return dummy.next
