"""
LeetCode 55 - Jump Game
Difficulty: Medium
Topic: Greedy

Problem Link:
https://leetcode.com/problems/jump-game/

====================================================
Approach 1: Recursion (Brute Force)
Time Complexity: O(2^n)
Space Complexity: O(n)
====================================================

class Solution:
    def canJump(self, nums):

        def dfs(index):

            if index >= len(nums) - 1:
                return True

            max_jump = nums[index]

            for jump in range(1, max_jump + 1):
                if dfs(index + jump):
                    return True

            return False

        return dfs(0)


====================================================
Approach 2: Dynamic Programming
Time Complexity: O(n²)
Space Complexity: O(n)
====================================================

class Solution:
    def canJump(self, nums):

        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(n):

            if dp[i]:

                for jump in range(1, nums[i] + 1):

                    if i + jump < n:
                        dp[i + jump] = True

        return dp[n - 1]


====================================================
Approach 3: Greedy (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def canJump(self, nums):

        max_reach = 0

        for i in range(len(nums)):

            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

        return True
