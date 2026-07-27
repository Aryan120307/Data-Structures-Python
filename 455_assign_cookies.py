"""
LeetCode 455 - Assign Cookies
Difficulty: Easy
Topic: Greedy

Problem Link:
https://leetcode.com/problems/assign-cookies/

====================================================
Approach 1: Brute Force
Time Complexity: O(n × m)
Space Complexity: O(1)
====================================================

class Solution:
    def findContentChildren(self, g, s):

        used = [False] * len(s)
        count = 0

        for child in g:

            for i in range(len(s)):

                if not used[i] and s[i] >= child:
                    used[i] = True
                    count += 1
                    break

        return count


====================================================
Approach 2: Greedy + Sorting + Two Pointers (Optimal)
Time Complexity: O(n log n + m log m)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def findContentChildren(self, g, s):

        g.sort()
        s.sort()

        child = 0
        cookie = 0

        while child < len(g) and cookie < len(s):

            if s[cookie] >= g[child]:
                child += 1

            cookie += 1

        return child
