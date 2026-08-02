"""
LeetCode 45 - Jump Game II
Difficulty: Medium
Topic: Greedy

Problem Link:
https://leetcode.com/problems/jump-game-ii/

====================================================
Approach 1: Recursion (Brute Force)
Time Complexity: O(2^n)
Space Complexity: O(n)
====================================================

class Solution:
    def jump(self, nums):

        def dfs(index):

            if index >= len(nums) - 1:
                return 0

            ans = float("inf")

            for jump in range(1, nums[index] + 1):
                ans = min(ans, 1 + dfs(index + jump))

            return ans

        return dfs(0)


====================================================
Approach 2: Dynamic Programming
Time Complexity: O(n²)
Space Complexity: O(n)
====================================================

class Solution:
    def jump(self, nums):

        n = len(nums)
        dp = [float("inf")] * n
        dp[0] = 0

        for i in range(n):

            for jump in range(1, nums[i] + 1):

                if i + jump < n:
                    dp[i + jump] = min(dp[i + jump], dp[i] + 1)

        return dp[-1]


====================================================
Approach 3: Greedy (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def jump(self, nums):

        if len(nums) <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
