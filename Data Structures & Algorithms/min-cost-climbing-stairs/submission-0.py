class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        stairs = [0] *n


        stairs[0] = cost[0]
        stairs[1] = cost[1]

        for i in range(2, n,1):
            stairs[i] = min(cost[i]+stairs[i-1],cost[i]+stairs[i-2])

        return min(stairs[n-1],stairs[n-2])