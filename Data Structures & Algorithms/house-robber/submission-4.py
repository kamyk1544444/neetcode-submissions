class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        rob1,rob2 = 0,0

        for i in range(0,n,1):
            temp = max(rob2+nums[i],rob1)
            rob2 = rob1
            rob1 = temp
            
        
        return rob1

         