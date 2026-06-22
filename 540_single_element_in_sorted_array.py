"""
LeetCode 540 - Single Element in a Sorted Array
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/single-element-in-a-sorted-array/

====================================================
Approach 1: Linear Pair Check
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def singleNonDuplicate(self, nums):
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]

        return nums[-1]


====================================================
Approach 2: Binary Search (Optimal)
Time Complexity: O(log n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def singleNonDuplicate(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Even index
            if mid % 2 == 0:

                if nums[mid] == nums[mid + 1]:
                    left = mid + 2
                else:
                    right = mid

            # Odd index
            else:

                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left]
