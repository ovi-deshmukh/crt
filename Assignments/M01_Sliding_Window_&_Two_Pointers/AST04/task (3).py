def pairInSortedRotated(arr, target):  
   n = len(arr)
   if n < 2:
      return False

   start = 0
   for i in range(n - 1):
      if arr[i] > arr[i + 1]:
         start = i + 1
         break
   end = (start - 1) % n

   while start != end:
      total = arr[start] + arr[end]
      if total == target:
         return True
      if total < target:
         start = (start + 1) % n
      else:
         end = (end - 1) % n

   return False


if __name__ == '__main__':
   arr = list(map(int,input().split()))
   target = int(input())
   print(pairInSortedRotated(arr,target))
