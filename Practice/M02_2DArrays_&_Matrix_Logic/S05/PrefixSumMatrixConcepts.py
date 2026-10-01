#Leet Code : 1314

#1314
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                row_start = max(0, i-k)
                row_end = min(row -1, i+k)

                col_start = max(0, j-k)
                col_end = min(col -1, j+k)

                total = 0
                for r in range(row_start, row_end+1):
                    for c in range(col_start, col_end+1):
                        total += mat[r][c]
                res[i][j] = total
        return res
        