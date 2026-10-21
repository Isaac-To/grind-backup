"""
121. Best Time to Buy And Sell Stock  [Easy]  (Sliding Window)

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Statement: best-time-to-buy-and-sell-stock.md   ·   Fluency target: 15 min (prior)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        diff = 0
        min_price = int(1e9)
        for price in prices:
            min_price = min(min_price, price)
            diff = max(diff, price - min_price)
        return diff

TESTS = [
    (([7, 1, 5, 3, 6, 4],), 5),
    (([7, 6, 4, 3, 1],), 0),
]
