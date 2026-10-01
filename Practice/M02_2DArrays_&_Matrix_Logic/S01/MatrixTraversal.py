'''
2D --> It contains of 2 Dimensions
1. row
2. columns
The data can be store in the form of "Matrix"

Matrix Traversal: 
Ex: arr= [
[1,2,3],[4,5,6],[7,8,9]]

1  2  3
4  5  6 
7  8  9

arr[0][0]=1
arr[0][1]=2
arr[0][2]=3
---------
---------
---------


'''
#Leet Code : 1572 
#Traditional Aprroach:
'''
n = len(mat)
total = 0
for i in range(n):
    for j in range(n):
        if i == j:
            total += mat[i][j]
        elif i + j == n -1:
            total += mat[i][j]
return total
Tim Complexity: O(n**2)
#Optimal Solution:
n = len(mat)
total = 0
for i in range(n):
    total += mat[i][i]
    total += mat[i][n-1-i]
if n % 2 == 1:
    total -= mat[n//2][n//2]
return total

'''
#498
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        result = []

        for d in range(rows + cols - 1):
            dia = []
            r = 0 if d < cols else d-cols+1
            c = d if d < cols else cols-1
            while r < rows and c >=0:
                dia.append(mat[r][c])
                r += 1
                c -=1
            if d % 2 == 0:
                dia.reverse()
            result.extend(dia)
        return result