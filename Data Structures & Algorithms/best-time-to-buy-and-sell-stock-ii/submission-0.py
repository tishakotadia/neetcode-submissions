class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=prices[i]-prices[i-1]
        return profit

# 7,1,3,6,4,5
# profit=2+3+1=6