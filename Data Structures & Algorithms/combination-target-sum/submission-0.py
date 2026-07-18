class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(start: int ,suma: int,  lista: List[int]):

            if suma == target:
                res.append(lista.copy())
                return
            if suma > target:
                return

            for i in range(start,len(nums)):
                lista.append(nums[i])
                dfs(i,suma+nums[i],lista)
                lista.pop()

        dfs(0,0,[])

        return res
