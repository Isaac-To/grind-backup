"""
792. Binary Search  [Easy]  (Binary Search)

https://leetcode.com/problems/binary-search/
Statement: binary-search.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

TESTS = [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
    (([], 5), -1),
    (([5], 5), 0),
    (([1, 2, 3], 0), -1),
    (([1, 2], 3), -1),
]
