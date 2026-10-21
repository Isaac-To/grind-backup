"""
125. Valid Palindrome  [Easy]  (Two Pointers)

https://leetcode.com/problems/valid-palindrome/
Statement: valid-palindrome.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

TESTS = [
    (('A man, a plan, a canal: Panama',), True),
    (('race a car',), False),
    ((' ',), True),
]
