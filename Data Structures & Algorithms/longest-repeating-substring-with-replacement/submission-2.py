class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l,wynik,cur = 0,0,0

        lista = defaultdict(int)

        for p in range(len(s)):

            lista[s[p]] += 1

            ile = max(lista.values())

            if (p-l+1)-ile > k:
                lista[s[l]] -=1
                l +=1

            wynik = max(wynik,p-l+1)

        return wynik
