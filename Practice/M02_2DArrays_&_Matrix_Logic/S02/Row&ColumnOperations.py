'''
Row & Column Operations:
'''
# Leet Code : 1351
#Traditional Approach:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows  = len(grid)
        col = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(col):
                if grid[r][c] < 0:
                    count +=1 
        return count

#Optimal Solution:      
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])

        r = rows - 1
        c = 0 
        count = 0
        while r>= 0 and  c < col:
            if grid[r][c] < 0:
                count += col - c
                r -= 1
            else: 
                c += 1
        return count


# Leet Code : 832
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #Traditional Approach:
        '''for row in image:
            row.reverse()
            for j in range(len(row):
                row[j] = 1 - row[j]
        return image'''
        #Optimal Solution:
        for row in image:
            left = 0
            right = len(row) - 1
            while left <= right:
                row[left] , row[right] = 1-row[right] , 1-row[left]
                left+=1
                right-=1
        return image
        
        