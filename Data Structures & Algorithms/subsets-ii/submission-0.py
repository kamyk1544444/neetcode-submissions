class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        wynik = []

        nums.sort()

        def dfs(index :int, sub: List[int]):

            
            
            if index >= len(nums):  
                
                return
            
            for i in range(index,len(nums)):

                if i>index and nums[i] == nums[i-1]:
                    continue
                
                
                sub.append(nums[i])
                wynik.append(sub.copy())
                dfs(i+1,sub)

                sub.pop()
        dfs(0,[])

        wynik.append([])
        
        return wynik