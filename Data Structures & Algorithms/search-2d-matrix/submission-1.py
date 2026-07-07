class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j= 0,0
        pos = matrix[i][j]

        while i != len(matrix) and matrix[i][j] <= target:
            if pos == target:
                return True
            i +=1
        i -=1
        l,r = 0,len(matrix[0])-1

        if i < 0:
            i=0

        while r >= l:
            
            mid = l + (r-l) // 2

            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False