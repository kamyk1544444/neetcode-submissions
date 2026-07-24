class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stack = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        wynik = []

        if len(digits) == 0:
            return wynik

        def backtrack(index: int,slowo: str):
            
            if index >= len(digits):
                wynik.append(slowo)
                return

            

            for i in range(len(stack[digits[index]])):
                backtrack(index+1,slowo+stack[digits[index]][i])
                

        
        backtrack(0,"")


        return wynik