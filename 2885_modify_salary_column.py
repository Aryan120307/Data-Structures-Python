"""
LeetCode 2885 - Modify Salary Column
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/modify-salary-column/

====================================================
Approach 1: Modify Existing Column (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
