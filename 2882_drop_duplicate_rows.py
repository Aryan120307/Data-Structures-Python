"""
LeetCode 2882 - Drop Duplicate Rows
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/drop-duplicate-rows/

====================================================
Approach 1: drop_duplicates() (Optimal)
Time Complexity: O(n)
Space Complexity: O(n)
====================================================
"""

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])
