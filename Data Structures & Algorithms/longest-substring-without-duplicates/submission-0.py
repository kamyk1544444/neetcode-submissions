class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = 0
        milosc = 0
        znaki = set()

        for r in range(len(s)):
            while s[r] in znaki:
                znaki.remove(s[l])
                l +=1
            znaki.add(s[r])
            milosc = max(milosc,r-l+1)
        
        return milosc
        

