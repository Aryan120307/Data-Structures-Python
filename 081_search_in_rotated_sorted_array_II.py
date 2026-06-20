"""
LeetCode 81 - Search in Rotated Sorted Array II
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

====================================================
Approach 1: Linear Search
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def search(self, nums, target):
        for num in nums:
            if num == target:
                return True
        return False


====================================================
Approach 2: Python Built-in Search
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def search(self, nums, target):
        return target in nums


====================================================
Approach 3: Modified Binary Search (Optimal)
Time Complexity: O(log n) Average
Worst Case: O(n) (due to duplicates)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def search(self, nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue

            # Left half sorted
            if nums[low] <= nums[mid]:

                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            # Right half sorted
            else:

                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False
