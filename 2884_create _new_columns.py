"""
LeetCode 2884 - Modify Columns
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/modify-columns/

====================================================
Approach 1: Create a New Column (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees
