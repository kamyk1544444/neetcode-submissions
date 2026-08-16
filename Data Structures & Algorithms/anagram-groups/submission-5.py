class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        slownik = defaultdict(list)
                  
        for slowo in strs:

            temp = "".join(sorted(slowo))

            slownik[temp].append(slowo)
        
        return list(slownik.values())