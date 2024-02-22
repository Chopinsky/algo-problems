'''
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: n = 3, trust = [[1,2],[2,3]]
Output: -1

Example 5:

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Constraints:

1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''


from typing import List
from collections import defaultdict

class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    cand = set(i for i in range(1, n+1))
    count = defaultdict(int)
    
    for a, b in trust:
      cand.discard(a)
      count[b] += 1
      
    for a in cand:
      if count[a] == n-1:
        return a
    
    return -1
  
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    cand = set([i for i in range(n)])
    c = [0] * n
    judge = -1
    
    for a, b in trust:
      a -= 1
      b -= 1
      
      if a in cand:
        cand.discard(a)
        
      c[b] += 1
      
    for j in cand:
      if c[j] == n-1:
        if judge >= 0:
          return -1
        
        judge = j
    
    return judge+1 if judge >= 0 else -1
    
    
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    if n == 1:
      return 1 if not trust else -1
      
    trusted = defaultdict(int)
    trust_others = set()
    
    for u, v in trust:
      trust_others.add(u)
      trusted[v] += 1
      
    for i, c in trusted.items():
      if c == n-1 and i not in trust_others:
        return i
    
    return -1
  