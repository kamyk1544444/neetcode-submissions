class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        stack ={}


        for i,n in enumerate(nums):
            diff = target - n
            if diff in stack:
                return [stack[diff],i]
            stack[n] = i