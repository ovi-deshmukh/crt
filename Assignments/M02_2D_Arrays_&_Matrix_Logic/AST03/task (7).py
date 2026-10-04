#Tasks
def diagonalDifference(arr):
    n = len(arr)
    primary_sum = sum(arr[i][i] for i in range(n))
    secondary_sum = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
