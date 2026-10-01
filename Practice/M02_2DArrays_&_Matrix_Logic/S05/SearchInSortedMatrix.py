#Leet Code : 74
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''for row in matrix:
            if target in row:
                return True
        return False'''
        row , col = len(matrix), len(matrix[0])
        left , right = 0, (row * col) - 1  #(3*3)-1=>8
        while left <= right:
            mid = (left + right) // 2
            r = mid // col
            c = mid % col
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                left = mid +1
            else:
                right  = mid -1
        return False

#Leet Code : 240    
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''row , col = len(matrix), len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == target:
                    return True
        return False'''
        row , col = len(matrix), len(matrix[0])
        r = 0 
        c = col -1
        while r < row and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r +=1
            else:
                c -= 1
        return False


      