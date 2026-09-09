class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(s)<len(t):
            return ""

        count1 = Counter(t)
        req = len(count1)

        print(count1)


        left=0
        res = (0,float("inf"))
        have = 0
        count2 = {}
        
        for right in range(len(s)):
            c = s[right]

            count2[c] = count2.get(c,0)+1


            if count1[c]==count2[c]:
                have +=1

            while have==req:

                ch = s[left]

                if res[1]-res[0] > right-left:
                    res = (left,right)

                count2[ch] = count2.get(ch,0)-1

                if count2[ch]+1 == count1[ch]:
                    have -=1
                
                left +=1
    
        return s[res[0]:res[1]+1] if res[1] != float("inf") else ""