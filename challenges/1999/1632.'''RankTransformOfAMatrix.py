'''
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

The rank is an integer starting from 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
It is guaranteed that answer is unique under the given rules.

Example 1:

Input: matrix = [[1,2],[3,4]]
Output: [[1,2],[2,3]]
Explanation:
The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.

Example 2:

Input: matrix = [[7,7],[7,7]]
Output: [[1,1],[1,1]]

Example 3:

Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

Example 4:

Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
Output: [[5,1,4],[1,2,3],[6,3,1]]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 500
-10 ** 9 <= matrix[row][col] <= 10 ** 9
'''


from typing import List
from collections import defaultdict


class Solution:
  '''
  Idea is to fill the answer matrix from the minimum numbers to the maximum
  numbers from the original matrix, with increamental ranks -- i.e. 
  rank[i][j] = max(rank[i][*], rank[*][j])+1 for all numbers that are smaller
  to the number in the cell.

  Trick is the "equal numbers". Need to use union-find to group all equal
  numbers from the same rows / columns together, and take the maximum score
  in this unioned busket of cells.
  '''
  def matrixRankTransform(self, mat: List[List[int]]) -> List[List[int]]:
    h, w = len(mat), len(mat[0])
    rows = [0] * h
    cols = [0] * w
    ans = [[0]*w for _ in range(h)]
    ids = [(i*w+j) for i in range(h) for j in range(w)]
    
    nums = []
    pos = defaultdict(list)
    
    for i in range(h):
      for j in range(w):
        val = mat[i][j]
        if val not in pos:
          nums.append(val)
          
        pos[val].append((i, j))
        
    nums.sort()
    # print(nums, pos)
    
    def union(a: int, b: int) -> int:
      ba, bb = find(a), find(b)
      
      if ba < bb:
        ids[bb] = ba
        return ba
      
      ids[ba] = bb
      return bb
      
    def find(a: int) -> int:
      while ids[a] != a:
        a = ids[a]
        
      return a
    
    for n in nums:
      r, c = {}, {}
      rank = defaultdict(int)
      cand = []
      
      for i, j in pos[n]:
        key = i*w+j
        rs, cs = 0, 0
        score = max(rows[i]+1, cols[j]+1)
        
        if i in r:
          rbase = find(r[i])
          rs = rank[rbase]
          key = union(key, rbase)
        else:
          r[i] = key
          
        if j in c:
          cbase = find(c[j])
          cs = rank[cbase]
          key = union(key, cbase)
        else:
          c[j] = key
          
        rank[key] = max(rank[key], rs, cs, score)
        
      for i, j in pos[n]:
        base = find(i*w+j)
        score = rank[base]
        
        ans[i][j] = score
        rows[i] = score
        cols[j] = score
      
    return ans
  