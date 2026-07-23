"""
LeetCode 182 - Duplicate Emails
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/duplicate-emails/

====================================================
Approach 1: duplicated() + drop_duplicates() (Optimal)
Time Complexity: O(n)
Space Complexity: O(n)
====================================================
"""

import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return (
        person[person.duplicated(subset=["email"])]
        [["email"]]
        .drop_duplicates()
    )
