"""
LeetCode 1011 - Capacity To Ship Packages Within D Days
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

====================================================
Approach 1: Brute Force
Time Complexity: O((sum(weights) - max(weights)) * n)
Space Complexity: O(1)
====================================================

class Solution:
    def shipWithinDays(self, weights, days):

        def canShip(capacity):
            days_needed = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0
                current_weight += weight

            return days_needed <= days

        for capacity in range(max(weights), sum(weights) + 1):
            if canShip(capacity):
                return capacity


====================================================
Approach 2: Binary Search on Answer (Optimal)
Time Complexity: O(n * log(sum(weights)))
Space Complexity: O(1)
====================================================
"""

class Solution:
    def shipWithinDays(self, weights, days):

        left = max(weights)
        right = sum(weights)

        while left < right:

            mid = (left + right) // 2

            days_needed = 1
            current_weight = 0

            for weight in weights:

                if current_weight + weight > mid:
                    days_needed += 1
                    current_weight = 0

                current_weight += weight

            if days_needed <= days:
                right = mid
            else:
                left = mid + 1

        return left
