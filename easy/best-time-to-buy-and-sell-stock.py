'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in
the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = float('inf')
        profit = 0
        for price in prices:
            # if we are getting a cheaper price then we buy that
            if buy_price > price:
                buy_price = price
            else:
                # otherwise if buy price at the moment is smaller or equal to current price
                # then we try our luck and get profits by selling
                profit = max(profit, price - buy_price)
        return profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window technique
        profit = 0
        l, r = 0, 1  # left = buy right=sell

        while r < len(prices):
            # now we need to check if this is a profitable transaction
            if prices[l] < prices[r]:
                profit = max(profit, prices[r] - prices[l])
            else:
                # if it reaches here then we have actually found the lowest current point
                l = r
            r += 1
        return profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])

            r += 1

        return profit


s = Solution2()
print(s.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
