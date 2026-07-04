class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       
        operacje = {
        "+": lambda a,b: a+b,
        "-": lambda a,b: a-b,
        "*": lambda a,b: a*b,
        "/": lambda a,b: int(a/b)
       }

        liczby = []

        for tok in tokens:

            if tok in operacje:
                n = liczby.pop()
                m = liczby.pop()

                wynik = operacje[tok](m,n)

                liczby.append(wynik)
            else:
                liczby.append(int(tok))

      
        return liczby.pop()