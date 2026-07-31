"""
LeetCode 2883 - Drop Missing Data
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/drop-missing-data/

====================================================
Approach 1: dropna() (Optimal)
Time Complexity: O(n)
Space Complexity: O(n)
====================================================
"""

import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
