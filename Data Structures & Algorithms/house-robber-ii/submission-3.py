class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        
        def robery(lista: List[int])->int:
            rob1,rob2 = 0,0
            for l in lista:
                temp = max(rob2+l,rob1)
                rob2 = rob1
                rob1 = temp
            return rob1

        
        return max(robery(nums[1:]), robery(nums[:-1]))

