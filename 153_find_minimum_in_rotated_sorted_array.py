"""
LeetCode 153 - Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

====================================================
Approach 1: Linear Search (Brute Force)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def findMin(self, nums):
        minimum = nums[0]

        for num in nums:
            minimum = min(minimum, num)

        return minimum


====================================================
Approach 2: Using Python min()
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def findMin(self, nums):
        return min(nums)


====================================================
Approach 3: Binary Search (Optimal)
Time Complexity: O(log n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def findMin(self, nums):
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
