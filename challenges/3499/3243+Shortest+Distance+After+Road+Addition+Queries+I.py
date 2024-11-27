'''
3243. Shortest Distance After Road Addition Queries I

8
[[1,5],[0,2],[2,6]]
6
[[1,3],[3,5]]
'''

class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    d = [n-1-i for i in range(n)]
    p = [set([i-1] if i > 0 else []) for i in range(n)]
    # print('init:', d, p)
    ans = []
    
    def update(u: int, v: int):
      p[v].add(u)
      if d[u] <= d[v]+1:
        # no nodes get better dist
        return
      
      d[u] = d[v]+1
      stack = [(d[u], u)]
      
      while stack:
        dist, u = heappop(stack)
        for v in p[u]:
          if d[v] <= dist+1:
            continue
            
          d[v] = dist+1
          heappush(stack, (d[v], v))
    
    for u, v in queries:
      update(u, v)
      # print('iter:', (u, v), d, p)
      ans.append(d[0])
    
    return ans
        