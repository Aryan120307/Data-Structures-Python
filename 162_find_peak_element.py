"""
LeetCode 162 - Find Peak Element
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/find-peak-element/

====================================================
Approach 1: Linear Scan
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def findPeakElement(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


====================================================
Approach 2: Binary Search (Optimal)
Time Complexity: O(log n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (
                (mid == 0 or nums[mid] > nums[mid - 1])
                and
                (mid == len(nums) - 1 or nums[mid] > nums[mid + 1])
            ):
                return mid

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid - 1

        return -1
