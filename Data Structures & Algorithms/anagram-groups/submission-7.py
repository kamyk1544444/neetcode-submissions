class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ret = {}
        for word in strs:

            srt = "".join(sorted(word))

            if srt not in ret:
                ret[srt] = []
            
            ret[srt].append(word)

        return list(ret.values())