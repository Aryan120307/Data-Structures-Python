"""
LeetCode 58 - Length of Last Word
Difficulty: Easy
Topic: Strings

Problem Link:
https://leetcode.com/problems/length-of-last-word/

Approach:
Split the string into words and return the length of the last word.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
