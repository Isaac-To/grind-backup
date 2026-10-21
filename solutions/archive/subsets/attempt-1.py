"""
78. Subsets  [Medium]  (Backtracking)

https://leetcode.com/problems/subsets/
Statement: subsets.md   ·   Fluency target: 30 min (prior)
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        pass

TESTS = [
    (([1, 2, 3],), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    (([0],), [[], [0]]),
    (([-3],), [[], [-3]]),
    (([10, -10],), [[], [10], [10, -10], [-10]]),
]
