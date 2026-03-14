"""
LeetCode 367 - Valid Perfect Square
Difficulty: Easy
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/valid-perfect-square/

Approach:
Check numbers whose square equals num.

Time Complexity: O(√n)
Space Complexity: O(1)
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            if i * i == num:
                return True
            if i * i > num:
                return False
