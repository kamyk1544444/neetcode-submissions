class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        lista = defaultdict(list)

        for word in strs:
            s = "".join(sorted(word))
            lista[s].append(word)
        
        return list(lista.values())