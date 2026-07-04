class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for i in strs:
            m = ''.join(sorted(i))
            res[m].append(i)
        return list(res.values())

        