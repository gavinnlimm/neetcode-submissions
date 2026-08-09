class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                potential = prices[j] - prices[i]
                if (maxProfit < potential):
                    maxProfit = potential
        
        return maxProfit
            
        