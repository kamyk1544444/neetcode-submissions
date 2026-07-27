class Solution:
    def climbStairs(self, n: int) -> int:
        
        stairs  = [0]*n

        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 3

        stairs[0],stairs[1],stairs[2] = 1,2,3

        for i in range(2,n,1):
            stairs[i] = stairs[i-2]+stairs[i-1]
        
        return stairs[n-1]