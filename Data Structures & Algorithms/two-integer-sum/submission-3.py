class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        slownik = {}

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in slownik:
                return [slownik[diff],i]

            slownik[nums[i]] = i
        
        
        return [0,8]


