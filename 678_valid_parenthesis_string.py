"""
LeetCode 678 - Valid Parenthesis String
Difficulty: Medium
Topic: Greedy

Problem Link:
https://leetcode.com/problems/valid-parenthesis-string/

====================================================
Approach 1: Recursion (Brute Force)
Time Complexity: O(3^n)
Space Complexity: O(n)
====================================================

class Solution:
    def checkValidString(self, s):

        def dfs(index, balance):

            if balance < 0:
                return False

            if index == len(s):
                return balance == 0

            if s[index] == '(':
                return dfs(index + 1, balance + 1)

            elif s[index] == ')':
                return dfs(index + 1, balance - 1)

            else:
                return (
                    dfs(index + 1, balance + 1) or
                    dfs(index + 1, balance - 1) or
                    dfs(index + 1, balance)
                )

        return dfs(0, 0)


====================================================
Approach 2: Greedy (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

class Solution:
    def checkValidString(self, s):

        min_open = 0
        max_open = 0

        for ch in s:

            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else:
                min_open -= 1
                max_open += 1

            if max_open < 0:
                return False

            if min_open < 0:
                min_open = 0

        return min_open == 0
