'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''

class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    edges = collections.defaultdict(list)
    for [a, b] in connections:
      edges[a].append(b)
      edges[b].append(a)

    ans = []
    rank = [-1] * n

    ```
    Think about the undirected graph as a tree, we start from root (v0) and dfs down, if the children of the current node can trace back to nodes of equal or lower depths, meaning there's a cycle, and attach the current node to the root node of this cycle; otherwise, there's no way around, and the path is critical.
    ```
    def dfs(v: int, p: int, depth: int) -> int:
      rank[v] = depth

      for w in edges[v]:
        if w == p:
          continue

        # vertex hasn't been visited yet
        if rank[w] < 0:
          rank[w] = dfs(w, v, depth+1)

        if depth < rank[w]:
          # path between v and w is critical, because there's no way to trace from w
          # to a lower level
          ans.append([v, w])
        else:
          # path is not critical, w can be traced to a node with lower levels, update
          # v's rank to merge it into this cycle as well
          rank[v] = min(rank[v], rank[w])

      return rank[v]

    dfs(0, 0, 0)
    # print(rank)

    return ans
