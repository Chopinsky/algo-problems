'''
6163. Build a Matrix With Conditions

You are given a positive integer k. You are also given:

a 2D integer array rowConditions of size n where rowConditions[i] = [abovei, belowi], and
a 2D integer array colConditions of size m where colConditions[i] = [lefti, righti].
The two arrays contain integers from 1 to k.

You have to build a k x k matrix that contains each of the numbers from 1 to k exactly once. The remaining cells should have the value 0.

The matrix should also satisfy the following conditions:

The number abovei should appear in a row that is strictly above the row at which the number belowi appears for all i from 0 to n - 1.
The number lefti should appear in a column that is strictly left of the column at which the number righti appears for all i from 0 to m - 1.
Return any matrix that satisfies the conditions. If no answer exists, return an empty matrix.

Example 1:

Input: k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]
Output: [[3,0,0],[0,0,1],[0,2,0]]
Explanation: The diagram above shows a valid example of a matrix that satisfies all the conditions.
The row conditions are the following:
- Number 1 is in row 1, and number 2 is in row 2, so 1 is above 2 in the matrix.
- Number 3 is in row 0, and number 2 is in row 2, so 3 is above 2 in the matrix.
The column conditions are the following:
- Number 2 is in column 1, and number 1 is in column 2, so 2 is left of 1 in the matrix.
- Number 3 is in column 0, and number 2 is in column 1, so 3 is left of 2 in the matrix.
Note that there may be multiple correct answers.
Example 2:

Input: k = 3, rowConditions = [[1,2],[2,3],[3,1],[2,3]], colConditions = [[2,1]]
Output: []
Explanation: From the first two conditions, 3 has to be below 1 but the third conditions needs 3 to be above 1 to be satisfied.
No matrix can satisfy all the conditions, so we return the empty matrix.

Constraints:

2 <= k <= 400
1 <= rowConditions.length, colConditions.length <= 10^4
rowConditions[i].length == colConditions[i].length == 2
1 <= abovei, belowi, lefti, righti <= k
abovei != belowi
lefti != righti
'''

from typing import List, Dict, Set
from collections import defaultdict


class Solution:
  def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
    ans = [[0]*k for _ in range(k)] 
    rows = defaultdict(set)
    cols = defaultdict(set)
    reverse_rows = defaultdict(set)
    reverse_cols = defaultdict(set)
    rc = defaultdict(int)
    cc = defaultdict(int)
    
    for u, v in rowConditions:
      rows[u].add(v)
      reverse_rows[v].add(u)
      rc[u] = len(rows[u])
      
    for u, v in colConditions:
      cols[u].add(v)
      reverse_cols[v].add(u)
      cc[u] = len(cols[u])
      
    # check if we're in a cycle using dfs
    def dfs(u: int, graph: Dict, path: Set, visited: Set) -> bool:
      if u in path:
        return False
      
      if u in visited:
        return True
      
      visited.add(u)
      
      # end of the path
      if u not in graph:
        return True
      
      path.add(u)
      for v in graph[u]:
        if not dfs(v, graph, path, visited):
          return False
        
      path.discard(u)
      return True
    
    def check(src: Dict) -> bool:
      seen = set()
      path = set()
      
      for i in range(1, k+1):
        if i in seen:
          continue
          
        path.clear()
        if not dfs(i, src, path, seen):
          # print('found cycle', src)
          return False
        
      return True
    
    if not check(rows) or not check(cols):
      return []
    
    # use topological sort to assign row/col indexs
    def assign(src: Dict, counter: Dict) -> Dict:
      index = defaultdict(int)
      curr = k-1
      stack = []
      
      for u in range(1, k+1):
        if u not in counter:
          index[u] = curr
          curr -= 1
          
          for v in src[u]:
            counter[v] -= 1
            if not counter[v]:
              stack.append(v)
              
      # print('assign:', src, stack)
      while stack:
        u = stack.pop()
        index[u] = curr
        curr -= 1
        
        for v in src[u]:
          counter[v] -= 1
          if not counter[v]:
            stack.append(v)
      
      return index
      
    row_index = assign(reverse_rows, rc)
    col_index = assign(reverse_cols, cc)
    # print(row_index, col_index)
    
    for i in range(1, k+1):
      if i in row_index and i in col_index:
        r, c = row_index[i], col_index[i]
        # print(i, r, c)
        ans[r][c] = i
    
    return ans
    