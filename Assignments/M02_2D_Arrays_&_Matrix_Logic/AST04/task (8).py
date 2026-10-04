def diagonalSort(mat):
   if not mat or not mat[0]:
      return mat

   rows, cols = len(mat), len(mat[0])

   for start_row in range(rows):
      diagonal = []
      row, col = start_row, 0
      while row < rows and col < cols:
         diagonal.append(mat[row][col])
         row += 1
         col += 1
      diagonal.sort()

      row, col = start_row, 0
      for value in diagonal:
         mat[row][col] = value
         row += 1
         col += 1

   for start_col in range(1, cols):
      diagonal = []
      row, col = 0, start_col
      while row < rows and col < cols:
         diagonal.append(mat[row][col])
         row += 1
         col += 1
      diagonal.sort()

      row, col = 0, start_col
      for value in diagonal:
         mat[row][col] = value
         row += 1
         col += 1

   return mat
if __name__ == '__main__':
   m, n = map(int, input().split())
   mat = []
   for i in range(m):
      mat.append(list(map(int, input().split())))
   print(diagonalSort(mat))
