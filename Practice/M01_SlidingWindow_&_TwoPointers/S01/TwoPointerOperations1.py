'''Two Pointers:
Definition: Two pointers is a technique that uses two pointers to iterate through a data structure, 
such as an array or a linked list, to solve problems efficiently. 
Types:
1. opposite direction: In this type, two pointers are initialized at the beginning and end of the data structure,Opposite direction 
2. same direction: In this type, two pointers are initialized at the same position and move in the same direction through the data structure.

Two Sum :

arr=[2,3,4,5,6]
target=11
found =False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            found=True
            print("Pair found at index",i,"and",j)
            break
    if found:
        break
if not found:
    print("Pair not found")
'''
arr=[2,3,4,5,6]
target=11
found =False
left,right=0,len(arr)-1
while left<right:
    if arr[left]+arr[right]==target:
        found=True
        print("Pair found at index",left,"and",right)
        break
    elif arr[left]+arr[right]<target:
        left+=1
    else:
        right-=1
if not found:
    print("Pair not found")