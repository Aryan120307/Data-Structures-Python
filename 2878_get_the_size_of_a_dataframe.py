"""
LeetCode 2878 - Get the Size of a DataFrame
Difficulty: Easy
Topic: Pandas

Problem Link:
https://leetcode.com/problems/get-the-size-of-a-dataframe/

====================================================
Approach 1: Use DataFrame.shape (Optimal)
Time Complexity: O(1)
Space Complexity: O(1)
====================================================
"""

import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return list(players.shape)
