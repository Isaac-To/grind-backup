"""
789. Kth Largest Element In a Stream  [Easy]  (Heap / Priority Queue)

https://leetcode.com/problems/kth-largest-element-in-a-stream/
Statement: kth-largest-element-in-a-stream.md   ·   Fluency target: 15 min (prior)
"""


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        sorted_nums = sorted(self.nums)
        removed = sorted_nums[:len(self.nums) - self.k]
        preserved = sorted_nums[len(self.nums) - self.k:]
        self.nums = preserved
        return removed[0]

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

TESTS = [
    {"ops": ['KthLargest', 'add', 'add', 'add', 'add', 'add'], "args": [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]], "want": [None, 4, 5, 5, 8, 8]},
    {"ops": ['KthLargest', 'add', 'add', 'add', 'add'], "args": [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]], "want": [None, 7, 7, 7, 8]},
    {"ops": ['KthLargest', 'add', 'add', 'add'], "args": [[1, []], [2], [1], [3]], "want": [None, 2, 2, 3]},
    {"ops": ['KthLargest', 'add', 'add', 'add', 'add'], "args": [[3, [2, 3]], [1], [4], [0], [9]], "want": [None, 1, 2, 2, 3]},
    {"ops": ['KthLargest', 'add', 'add'], "args": [[2, [-5, -1, -5]], [-5], [0]], "want": [None, -5, -1]},
]
