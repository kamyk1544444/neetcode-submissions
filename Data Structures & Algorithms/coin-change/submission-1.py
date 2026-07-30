
import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

       

        if amount==0:
            return 0

        dp = [sys.maxsize]* (amount+1)
        
        for coin in coins:
            if coin<=amount:
                dp[coin] = 1

        for i in range(1,amount):
            
            for coin in coins:
                if coin+i<= amount:
                    dp[coin+i] = min(dp[i]+1,dp[coin+i])
                    
                
           

        return dp[amount] if dp[amount] != sys.maxsize else -1
                  
