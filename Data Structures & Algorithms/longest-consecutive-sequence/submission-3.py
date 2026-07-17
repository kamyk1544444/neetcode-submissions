class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)  # Wrócenie do setu daje nam podgląd O(1)
        wynik = 0

        for n in num_set:
            # Sprawdzamy, czy 'n' to początek ciągu (czy ma lewego sąsiada?)
            if (n - 1) not in num_set:
                dlugosc = 1
                # Jeśli to początek, sprawdzamy jak daleki jest ten ciąg
                while (n + dlugosc) in num_set:
                    dlugosc += 1
                wynik = max(wynik, dlugosc)
                
        return wynik