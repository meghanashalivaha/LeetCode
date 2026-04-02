class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] → current row
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        # initialize (0,0)
        for k in range(3):
            if coins[0][0] < 0 and k > 0:
                dp[0][k] = 0
            else:
                dp[0][k] = coins[0][0]
        
        # first row
        for j in range(1, n):
            for k in range(3):
                val = coins[0][j]
                
                # take normally
                dp[j][k] = dp[j-1][k] + val
                
                # neutralize
                if val < 0 and k > 0:
                    dp[j][k] = max(dp[j][k], dp[j-1][k-1])
        
        # process remaining rows
        for i in range(1, m):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            
            # first column
            for k in range(3):
                val = coins[i][0]
                
                new_dp[0][k] = dp[0][k] + val
                
                if val < 0 and k > 0:
                    new_dp[0][k] = max(new_dp[0][k], dp[0][k-1])
            
            # rest of row
            for j in range(1, n):
                for k in range(3):
                    val = coins[i][j]
                    
                    # from top or left
                    best = max(dp[j][k], new_dp[j-1][k])
                    
                    # take normally
                    new_dp[j][k] = best + val
                    
                    # neutralize
                    if val < 0 and k > 0:
                        best2 = max(dp[j][k-1], new_dp[j-1][k-1])
                        new_dp[j][k] = max(new_dp[j][k], best2)
            
            dp = new_dp
        
        return max(dp[n-1])