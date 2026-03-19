"""
LeetCode 977 - Squares of a Sorted Array
Difficulty: Easy
Topic: Arrays, Two Pointers

Problem Link:
https://leetcode.com/problems/squares-of-a-sorted-array/

Approach:
Use two pointers (left and right) to compare absolute values.
Fill the result array from the end with the larger square.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return result
