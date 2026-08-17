class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            left , right =i+1,n-1
            if i>0 and nums[i-1] == nums[i]:
                continue
            while right>left:
                
                val = nums[left]+nums[i]+nums[right]

                if val == 0:
                    res.append([nums[left],nums[i],nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                elif val>0:
                    right -=1
                else:
                    left +=1
        return res
