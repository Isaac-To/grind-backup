"""
20. Valid Parentheses  [Easy]  (Stack)

https://leetcode.com/problems/valid-parentheses/
Statement: valid-parentheses.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = dict(zip(')]}', '([{'))
        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack

TESTS = [
    (('()',), True),
    (('()[]{}',), True),
    (('(]',), False),
    (('([])',), True),
    (('([)]',), False),
]
