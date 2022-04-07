"""
# Java
看了最高解感觉被题目带复杂了
class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int j = i + 1;
            if(prices[i] < prices[j]) {
                while(j < prices.length - 1) {
                    if(prices[j] < prices[j + 1]) {
                        j++;
                    } else {
                        break;
                    }
                }
                profit =profit + prices[j] - prices[i];
            }
            i = j - 1;
        }
        return profit;
    }
}
最优解 直接判断后一个是否比前一个大 然后累加，什么原理呢？
public class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        for (int i=0; i< prices.length-1; i++) {
            if (prices[i+1]>prices[i]) total += prices[i+1]-prices[i];
        }
        return total;
        }
}
"""
from matplotlib.mathtext import List

# 按照最优解思路实现
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] - prices[i] > 0:
                profit = profit + prices[i + 1] - prices[i]
        return profit
