"""
78. Subsets  [Medium]  (Backtracking)

https://leetcode.com/problems/subsets/
Statement: subsets.md   ·   Fluency target: 30 min (prior)
"""


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []

        def backtrack(start: int) -> None:
            res.append(subset.copy())
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res


TESTS = [
    (([1, 2, 3],), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    (([0],), [[], [0]]),
    (([-3],), [[], [-3]]),
    (([10, -10],), [[], [10], [10, -10], [-10]]),
]