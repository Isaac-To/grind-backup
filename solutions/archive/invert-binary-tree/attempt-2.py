"""
226. Invert Binary Tree  [Easy]  (Trees)

https://leetcode.com/problems/invert-binary-tree/
Statement: invert-binary-tree.md   ·   Fluency target: 15 min (prior)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root == None:
            return root
        l = self.invertTree(root.right)
        r = self.invertTree(root.left)
        nTree = TreeNode(
            val = root.val,
            left = l,
            right = r
        )
        return nTree


TESTS = [
    (([4, 2, 7, 1, 3, 6, 9],), [4, 7, 2, 9, 6, 3, 1]),
    (([2, 1, 3],), [2, 3, 1]),
    (([],), []),
    (([1],), [1]),
    (([1, 2, None, 3],), [1, None, 2, None, 3]),
    (([1, None, 2, None, 3],), [1, 2, None, 3]),
]
