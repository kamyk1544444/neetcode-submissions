class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        wynik = []

        nums.sort()

        def dfs(index: int, suma:int, sub: List[int]):

            if suma == target:
                wynik.append(sub.copy())
                return
            if suma > target:
                return
            
            for i in range(index,len(nums)):

                if i > index and nums[i] == nums[i-1]:
                    continue
                
                sub.append(nums[i])

                dfs(i+1,suma+nums[i],sub)

                sub.pop()

            
        
        dfs(0,0,[])

        return wynik
