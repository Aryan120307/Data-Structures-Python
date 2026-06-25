"""
LeetCode 875 - Koko Eating Bananas
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/koko-eating-bananas/

Approach 1: Brute Force
- Try every possible eating speed.
- Time Complexity: O(max(piles) * n)
- Space Complexity: O(1)

Approach 2: Binary Search on Answer (Optimal)
- Search for the minimum valid eating speed.
- Time Complexity: O(n * log(max(piles)))
- Space Complexity: O(1)
"""

class Solution:
    def minEatingSpeed(self, piles, h):

        left, right = 1, max(piles)
        answer = right

        while left <= right:

            mid = (left + right) // 2

            total_hours = 0

            for pile in piles:
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
