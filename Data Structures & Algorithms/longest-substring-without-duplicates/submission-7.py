class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        count = {}
        left = 0
        res = 0

        for right in range(len(s)):

            if s[right] in count:
                left = max(count[s[right]]+1,left)
            count[s[right]] = right
            res = max(res,right-left+1)
        
        return res