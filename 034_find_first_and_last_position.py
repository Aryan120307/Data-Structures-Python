"""
LeetCode 34 - Find First and Last Position of Element in Sorted Array
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

====================================================
Approach 1: Linear Search (Two Traversals)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def searchRange(self, nums, target):
        first = -1
        last = -1

        for i in range(len(nums)):
            if nums[i] == target:
                first = i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                last = i
                break

        return [first, last]


====================================================
Approach 2: Linear Search (Single Traversal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================

class Solution:
    def searchRange(self, nums, target):
        first = -1
        last = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]


====================================================
Approach 3: Binary Search (Optimal)
Time Complexity: O(log n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def searchRange(self, nums, target):

        def binarySearch(findFirst):
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid

                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1

                elif nums[mid] < target:
                    left = mid + 1

                else:
                    right = mid - 1

            return ans

        return [binarySearch(True), binarySearch(False)]
