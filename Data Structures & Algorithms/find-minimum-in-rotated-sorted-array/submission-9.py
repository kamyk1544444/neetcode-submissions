class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left,right = 0,len(nums)-1

        res = 10000

        while right>=left:

            mid = left+(right-left) // 2

            res = min(res,nums[mid])

            if nums[right] < nums[left]:
                
                if nums[mid] < nums[left]:
                    right = mid-1
                else:
                    left = mid+1

            else:
                right = mid-1
        
        return res