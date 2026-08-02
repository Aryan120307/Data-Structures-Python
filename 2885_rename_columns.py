"""
LeetCode 2885 - Rename Columns
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/rename-columns/

====================================================
Approach 1: rename() (Optimal)
Time Complexity: O(n)
Space Complexity: O(1)
====================================================
"""

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns={
            "id": "student_id",
            "first": "first_name",
            "last": "last_name",
            "age": "age_in_years"
        }
    )
