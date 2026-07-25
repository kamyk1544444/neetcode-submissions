class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        res = []
        
        # Słowniki do zapamiętywania wyników dla poszczególnych komórek,
        # żeby nie przetwarzać ich wielokrotnie i nie niszczyć oryginalnej mapy na stałe.
        pacific_memo = {}
        atlantic_memo = {}

        def can_reach_pacific(r: int, c: int, prev: int) -> bool:
            # 1. Poza mapą, pod górę, albo komórka odwiedzona w obecnej ścieżce (-2)
            if not (0 <= r < row) or not (0 <= c < col) or heights[r][c] == -2 or prev < heights[r][c]:
                return False 
            
            # 2. Sukces: dotarliśmy do brzegu Pacyfiku
            if r == 0 or c == 0:
                return True
                
            # 3. Jeśli już kiedyś sprawdziliśmy tę komórkę, zwracamy gotowy wynik
            if (r, c) in pacific_memo:
                return pacific_memo[(r, c)]

            temp = heights[r][c]
            heights[r][c] = -2  # Oznaczamy jako odwiedzony w tej konkretnej ścieżce

            # Sprawdzamy 4 kierunki
            found = (
                can_reach_pacific(r+1, c, temp) or
                can_reach_pacific(r-1, c, temp) or
                can_reach_pacific(r, c+1, temp) or 
                can_reach_pacific(r, c-1, temp) 
            )

            # ZAWSZE przywracamy oryginalną wysokość dla innych ścieżek i dla oceanu Atlantyckiego!
            heights[r][c] = temp  
            pacific_memo[(r, c)] = found
            return found

        def can_reach_atlantic(r: int, c: int, prev: int) -> bool:
            if not (0 <= r < row) or not (0 <= c < col) or heights[r][c] == -2 or prev < heights[r][c]:
                return False 
            
            # Sukces: dotarliśmy do brzegu Atlantyku
            if r == row - 1 or c == col - 1:
                return True
                
            if (r, c) in atlantic_memo:
                return atlantic_memo[(r, c)]

            temp = heights[r][c]
            heights[r][c] = -2

            found = (
                can_reach_atlantic(r+1, c, temp) or
                can_reach_atlantic(r-1, c, temp) or
                can_reach_atlantic(r, c+1, temp) or 
                can_reach_atlantic(r, c-1, temp) 
            )

            heights[r][c] = temp
            atlantic_memo[(r, c)] = found
            return found

        # Zamiast pętli po brzegach, iterujemy po CAŁEJ mapie.
        # Sprawdzamy dla każdej komórki z osobna, czy woda z niej dopłynie do Pacyfiku i do Atlantyku.
        for i in range(row):
            for j in range(col):
                if can_reach_pacific(i, j, heights[i][j]) and can_reach_atlantic(i, j, heights[i][j]):
                    res.append([i, j])

        return res