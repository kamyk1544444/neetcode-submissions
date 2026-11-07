class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        cont = set(nums)


        longest = 0 

        for num in nums:

            if num-1 not in cont:
                
                val = num
                temp_max = 0
                while val in cont:
                    temp_max +=1
                    val +=1
                
                longest = max(longest,temp_max)
        
        return longest


        

    