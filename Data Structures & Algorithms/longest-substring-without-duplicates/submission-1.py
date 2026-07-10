class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        lista = defaultdict(int)
        l = 0
        wynik = 0

        for p in range(len(s)):

            
            znak = s[p]
            lista[znak] +=1

            while lista[znak] > 1:
                lista[s[l]] -=1
                l +=1
            
            wynik = max(wynik,p-l+1)

        return wynik
