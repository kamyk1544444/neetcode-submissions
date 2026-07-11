class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""

        wartosci = [0]*128
        potrzeba = 0
        for i in range(len(t)):
            if wartosci[ord(t[i])] == 0:
                potrzeba +=1
            wartosci[ord(t[i])] +=1

        okno = [0]*128

        l=0

        
        mamy = 0
        minimal = [-1,-1]
        minimalwartosc = float("infinity")
        for r in range(len(s)):
            znak = ord(s[r])

            okno[znak] +=1

            if okno[znak] == wartosci[znak] and wartosci[znak] > 0:
                mamy +=1

            while potrzeba == mamy:
                znak2 = ord(s[l])

                if minimalwartosc > (r-l+1):
                    minimalwartosc = r-l+1
                    minimal = [l,r]

                if okno[znak2] == wartosci[znak2] and wartosci[znak2] > 0:
                    mamy -=1

                okno[znak2] -=1
                l +=1

        return s[minimal[0]:minimal[1] + 1] if minimalwartosc != float("infinity") else ""