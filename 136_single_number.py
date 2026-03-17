"""
LeetCode 136 - Single Number
Difficulty: Easy
Topic: Arrays

Problem Link:
https://leetcode.com/problems/single-number/

Approach:
Count the occurrences of each element.
Return the element that appears only once.

Time Complexity: O(n²)
Space Complexity: O(1)
"""

class Solution:
    def singleNumber(self, nums):
        for i in nums:
            count = 0
            for j in nums:
                if i == j:
                    count += 1
            if count == 1:
                return i
