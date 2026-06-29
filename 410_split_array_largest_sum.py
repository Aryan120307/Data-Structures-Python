"""
LeetCode 410 - Split Array Largest Sum
Difficulty: Hard
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/split-array-largest-sum/

====================================================
Approach 1: Brute Force
Time Complexity: Exponential (Not Feasible)
Space Complexity: O(k)
====================================================

Idea:
- Try every possible way to split the array into k subarrays.
- Calculate the largest subarray sum for each split.
- Return the minimum possible largest sum.

This approach leads to exponential complexity and exceeds time limits.


====================================================
Approach 2: Binary Search on Answer (Optimal)
Time Complexity: O(n * log(sum(nums)))
Space Complexity: O(1)
====================================================
"""

class Solution:
    def splitArray(self, nums, k):

        left = max(nums)
        right = sum(nums)
        answer = right

        def canSplit(max_sum):
            subarrays = 1
            current_sum = 0

            for num in nums:

                if current_sum + num > max_sum:
                    subarrays += 1
                    current_sum = num

                else:
                    current_sum += num

            return subarrays <= k

        while left <= right:

            mid = (left + right) // 2

            if canSplit(mid):
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
