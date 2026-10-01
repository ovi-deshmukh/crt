#LLeet Code : 54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0]) -1
        top = 0
        bottom = len(matrix) -1

        res = [] 
        while left <= right and top <= bottom:     #L->R , T-> B, R->L, B->T
            #Traverse Left to Right
            for j in range(left,right+1):
                res.append(matrix[top][j])
            top += 1
            #Traverse Top to Bottom
            for i in range(top,bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            #Traverse Right to Left
            if top <= bottom:
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            #Traverse Bottom to Top
            if left <= right:
                for i in range(bottom,top - 1,-1):
                    res.append(matrix[i][left])
                left += 1
        return res
        

#Leetcode: 59
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [ [0] * n for _ in  range(n)]
        left = 0
        right = n -1
        top = 0
        bottom = n -1

        num = 1
        while left <= right and top <= bottom:     #L->R , T-> B, R->L, B->T
            #Traverse Left to Right
            for j in range(left,right+1):
                res[top][j] =num
                num += 1
            top += 1
            #Traverse Top to Bottom
            for i in range(top,bottom + 1):
                res[i][right]=num
                num +=1
            right -= 1
            #Traverse Right to Left
            if top <= bottom:
                for j in range(right,left-1,-1):
                    res[bottom][j] = num
                    num += 1
                bottom -= 1
            #Traverse Bottom to Top
            if left <= right:
                for i in range(bottom,top - 1,-1):
                    res[i][left] = num
                    num +=1
                left += 1
        return res
        
        