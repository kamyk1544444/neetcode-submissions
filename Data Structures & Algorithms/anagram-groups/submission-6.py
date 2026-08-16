class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        slownik = defaultdict(list)
                  
        for slowo in strs:

            count = [0]*26

            for c in slowo:
                count[ord(c)-ord("a")] +=1
            
            slownik[tuple(count)].append(slowo)
        
        return list(slownik.values())