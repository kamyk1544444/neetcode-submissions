class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return False
        
        liczby, znaki = [],[]

        for tok in tokens:
            if tok == "+":
                m = liczby[-1]
                liczby.pop()
                n = liczby[-1]
                liczby.pop()

                wynik = int(n + m)

                liczby.append(wynik)

            elif tok == "-":
                m = liczby[-1]
                liczby.pop()
                n = liczby[-1]
                liczby.pop()

                wynik = int(n - m)

                liczby.append(wynik)

            elif tok == "/":
                m = liczby[-1]
                liczby.pop()
                n = liczby[-1]
                liczby.pop()

                wynik = int(n / m)

                liczby.append(wynik)

            elif tok == "*":
                m = liczby[-1]
                liczby.pop()
                n = liczby[-1]
                liczby.pop()

                wynik = int(n * m)

                liczby.append(wynik)

            else:
                liczby.append(int(tok));

        return liczby[-1]