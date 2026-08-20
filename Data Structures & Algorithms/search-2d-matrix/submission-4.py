class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        left, right = 0,len(matrix)-1
        mid = left + (right-left) // 2
        while right>=left:

            mid = left + (right-left) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                break;
            elif matrix[mid][0] > target:
                right = mid-1
            else:
                left = mid+1

        

        left1,right1 = 0,len(matrix[0])-1
        
        while right1>=left1:
            
            mid1 = left1 + (right1-left1) // 2
        
            if right1>=left1:
                if matrix[mid][mid1] == target:
                    return True
                elif matrix[mid][mid1] > target:
                    right1 = mid1-1
                else:
                    left1 = mid1+1
            
            

        return False