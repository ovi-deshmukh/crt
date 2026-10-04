#Task
from typing import List
def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]: 
   result = []
   r, c = rStart, cStart

   if 0 <= r < rows and 0 <= c < cols:
      result.append([r, c])

   directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
   step_length = 1
   direction_index = 0

   while len(result) < rows * cols:
      for _ in range(2):
         dr, dc = directions[direction_index]
         for _ in range(step_length):
            r += dr
            c += dc
            if 0 <= r < rows and 0 <= c < cols:
               result.append([r, c])
         direction_index = (direction_index + 1) % 4
      step_length += 1

   return result
   

if __name__ == '__main__':
   rows,cols,rStart,cStart = map(int,input().split())
   print(spiralMatrixIII(rows,cols,rStart,cStart))
