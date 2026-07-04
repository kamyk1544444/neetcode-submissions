class Solution:
    def isValid(self, s: str) -> bool:
        
        pary = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack,j = [],0

        for znak in s:
            if znak in pary:
                if not stack or stack[-1] != pary[znak]:
                    return False
                stack.pop()
            else:
                stack.append(znak)
        if stack:
            return False
        return True
