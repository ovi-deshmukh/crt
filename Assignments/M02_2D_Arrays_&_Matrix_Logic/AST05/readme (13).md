# Find sum of all Boundary and Diagonal element of a Matrix

Given a 2D array arr[][] of order NxN, the task is to find the sum of all the elements present in both the diagonals and boundary elements of the given arr[][]. 

### Example: 
```
Input: arr[][] = { {1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4} } 
Output: 40 

Explanation: 
The Sum of elements on the boundary is 1 + 2 + 3 + 4 + 4 + 4 + 4 + 3 + 2 + 1 + 1 + 1 = 30. 
The Sum of elements on the diagonals which do not intersect with the boundary elements is 2 + 3 + 2 + 3 = 10. 
Therefore the required sum is 30 + 10 = 40.

Input: arr[][] = { {1, 2, 3}, {1, 2, 3}, {1, 2, 3}} 
Output: 18 

Explanation: 
The Sum of elements on the boundary is 1 + 2 + 3 + 3 + 3 + 2 + 1 + 1 = 16. 
The Sum of elements on the diagonals which do not intersect with the boundary elements is 2. 
Therefore the required sum is 16 + 2 = 18.```
```

## Instructions
1. Write your solution in `task.py`
2. Do NOT modify `test_task.py`
3. Run tests locally before pushing

## Submission Rules
- Only `task.py` will be evaluated
