class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        count = set()

        left,right=0,0

        count.add(s[left])
        res = 1

        while right < len(s)-1:

            right +=1
           

            while s[right] in count:
                count.remove(s[left])
                left +=1

            count.add(s[right])
            res = max(res,right-left+1)


        return res