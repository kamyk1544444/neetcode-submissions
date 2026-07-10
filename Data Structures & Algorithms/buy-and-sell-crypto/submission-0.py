class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxkeep = 1101
        profit = 0

        for i in prices:
            if i < maxkeep:
                maxkeep = i
                continue
            profit = max(profit,i-maxkeep)
        return profit