"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List


class Solution:
    """
    暴力解法，超时
    """

    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            j = i + 1
            while j < len(prices):
                max_profit = max(max_profit, prices[j] - prices[i])
                j = j + 1

        return max_profit

    def maxProfit1(self, prices: List[int]) -> int:
        """
        :param prices:
        :return:
        """
        max_profit = 0
        min_price = int('inf')

        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == '__main__':
    so = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(so.maxProfit(prices))
