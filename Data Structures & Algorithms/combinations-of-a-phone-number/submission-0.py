class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        stack = []
        stack.append([["a"],["b"],["c"]])
        stack.append([["d"],["e"],["f"]])
        stack.append([["g"],["h"],["i"]])
        stack.append([["j"],["k"],["l"]])
        stack.append([["m"],["n"],["o"]])
        stack.append([["p"],["q"],["r"],["s"]])
        stack.append([["t"],["u"],["v"]])
        stack.append([["w"],["x"],["y"],["z"]])

        wynik = []

        if len(digits) == 0:
            return wynik

        def backtrack(index: int,slowo: str):
            
            if index >= len(digits):
                wynik.append(slowo)
                return

            znak = ord(digits[index])-50

            for i in range(len(stack[znak])):
                backtrack(index+1,slowo+stack[znak][i][0])
                

        znak = stack[ord(digits[0])-50][0][0]
        backtrack(0,"")


        return wynik