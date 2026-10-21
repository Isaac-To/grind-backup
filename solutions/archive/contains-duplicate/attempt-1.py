"""
217. Contains Duplicate  [Easy]  (Arrays & Hashing)

https://leetcode.com/problems/contains-duplicate/
Statement: contains-duplicate.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) != len(nums)

TESTS = [
    (([1, 2, 3, 1],), True),
    (([1, 2, 3, 4],), False),
    (([1, 1, 1, 3, 3, 4, 3, 2, 4, 2],), True),
]
