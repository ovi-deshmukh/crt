from typing import List
def diagonalBoundarySum(arr):
    n = len(arr)
    if n == 0:
        return 0

    cells = set()
    for i in range(n):
        # Boundary cells
        cells.update(((0, i), (n - 1, i), (i, 0), (i, n - 1)))
        # Main and secondary diagonal cells
        cells.update(((i, i), (i, n - 1 - i)))

    return sum(arr[row][col] for row, col in cells)

if __name__ == '__main__':
    n = int(input())
    mat = []
    for i in range(n):
        mat.append(list(map(int, input().split())))
    print(diagonalBoundarySum(mat))
