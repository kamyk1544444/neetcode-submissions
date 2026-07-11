class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        pier,drug = [0] * 26, [0] * 26

        for i in range(len(s1)):
            pier[ord(s1[i]) - ord('a')] +=1
            drug[ord(s2[i]) - ord('a')] +=1

        match = 0

        for i in range(26):
            if pier[i] == drug[i]:
                match +=1
            
        l = 0

        for p in range(len(s1),len(s2)):
            if match == 26:
                return True
            
            znak = ord(s2[p])-ord('a')
            drug[znak] +=1

            if pier[znak] == drug[znak]:
                match +=1
            elif pier[znak] + 1 == drug[znak]:
                match -=1

            znak = ord(s2[l])-ord('a')
            drug[znak] -=1

            if pier[znak] == drug[znak]:
                match +=1
            elif pier[znak]-1 == drug[znak]:
                match -=1
            l +=1
        return match == 26

