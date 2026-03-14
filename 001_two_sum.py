"""
LeetCode 001 - Two Sum
Difficulty: Easy
Topic: Array, Hash Table

Problem Link:
https://leetcode.com/problems/two-sum/

Approach:
Brute Force - check every pair of numbers.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
