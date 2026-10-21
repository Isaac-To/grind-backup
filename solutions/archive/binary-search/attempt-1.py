"""
792. Binary Search  [Easy]  (Binary Search)

https://leetcode.com/problems/binary-search/
Statement: binary-search.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, mid, right = 0, len(nums) // 2, len(nums)
        hist = (left, mid, right)
        while left != right:
            if nums[mid] <= target:
                left = mid
            elif nums[mid] >= target:
                right = mid
            mid = ((right - left) // 2) + left
            if (left, mid, right) == hist:
                break
            print(mid, left, right)
            hist = (left, mid, right)
        if nums[mid] != target:
            return -1
        return mid

TESTS = [
    (([-1, 0, 3, 5, 9, 12], 9), 4),
    (([-1, 0, 3, 5, 9, 12], 2), -1),
]
