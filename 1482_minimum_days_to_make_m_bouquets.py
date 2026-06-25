"""
LeetCode 1482 - Minimum Number of Days to Make m Bouquets
Difficulty: Medium
Topic: Binary Search

Problem Link:
https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

====================================================
Approach 1: Brute Force
Time Complexity: O((maxDay - minDay) * n)
Space Complexity: O(1)
====================================================

class Solution:
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            return bouquets >= m

        min_day = min(bloomDay)
        max_day = max(bloomDay)

        for day in range(min_day, max_day + 1):

            if canMakeBouquets(day):
                return day

        return -1


====================================================
Approach 2: Binary Search on Answer (Optimal)
Time Complexity: O(n * log(maxDay))
Space Complexity: O(1)
====================================================
"""

class Solution:
    def minDays(self, bloomDay, m, k):

        if m * k > len(bloomDay):
            return -1

        def canMakeBouquets(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if canMakeBouquets(mid):
                answer = mid
                right = mid - 1

            else:
                left = mid + 1

        return answer
