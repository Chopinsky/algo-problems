'''
1361. Validate Binary Tree Nodes

You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

Note that the nodes have no values and that we only use the node numbers in this problem.

Example 1:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
Output: true
Example 2:

Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
Output: false
Example 3:

Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
Output: false

Constraints:

n == leftChild.length == rightChild.length
1 <= n <= 10^4
-1 <= leftChild[i], rightChild[i] <= n - 1
'''


class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    p = [-1]*n
    seen = set([i for i in range(n)])
    cnt = 0
    
    for u, v in enumerate(leftChild):
      if v < 0:
        continue
        
      if p[v] >= 0:
        return False
      
      p[v] = u
      cnt += 1
      seen.discard(v)
      
    for u, v in enumerate(rightChild):
      if v < 0:
        continue
        
      if p[v] >= 0:
        return False
      
      p[v] = u
      cnt += 1
      seen.discard(v)
        
    if cnt != n-1 or len(seen) != 1:
      return False
    
    curr, nxt = list(seen), []
    found = 0
    # print('check:', curr)
    
    while curr:
      found += len(curr)
      
      for u in curr:
        l, r = leftChild[u], rightChild[u]
        if l in seen or r in seen:
          return False
        
        if l >= 0:
          seen.add(l)
          nxt.append(l)
          
        if r >= 0:
          seen.add(r)
          nxt.append(r)
      
      curr, nxt = nxt, curr
      nxt.clear()
      
    return found == n
  