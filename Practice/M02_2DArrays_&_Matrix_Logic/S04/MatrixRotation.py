#Leet Code : 48
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''n =len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()
        '''
        matrix[:] = [list(row)[::-1] for row in zip(*matrix)]

#Leet Code : 1886
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n =len(mat)
        for _ in range(4):
            if mat == target:
                return True
                for i in range(n):
                    for j in range(i+1, n):
                        mat[i][j],mat[j][i] = mat[j][i], mat[i][j]
                for row in mat:
                    row.reverse()
        return False
        