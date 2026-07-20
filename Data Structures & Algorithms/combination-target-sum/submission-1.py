class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(i,suma,sub):

            if suma == target:
                res.append(sub.copy())
                return
            elif suma > target:
                return

            for j in range(i,len(nums)):
                sub.append(nums[j])
                dfs(j,suma+nums[j],sub)
                sub.pop()

            

        dfs(0,0,[])

        return res
