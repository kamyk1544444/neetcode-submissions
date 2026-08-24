class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        count = [0]*26
        
        left=0
        res = 1
        one = 0
        char = 0

        for right in range(len(s)):

            znak = ord(s[right])-ord("A")
            
            count[znak] +=1

            one = max(one,count[znak])
            

            while right-left-one+1>k and left<right:
                
                znakleft = ord(s[left])-ord("A")
                count[znakleft] -=1
                    

                left +=1
            
            res = max(res,right-left+1)
        
        return res