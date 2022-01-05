'''
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.

Example 1:

Input: favorite = [2,2,1,2]
Output: 3
Explanation:
The above figure shows how the company can invite employees 0, 1, and 2, and seat them at the round table.
All employees cannot be invited because employee 2 cannot sit beside employees 0, 1, and 3, simultaneously.
Note that the company can also invite employees 1, 2, and 3, and give them their desired seats.
The maximum number of employees that can be invited to the meeting is 3. 
Example 2:

Input: favorite = [1,2,0]
Output: 3
Explanation: 
Each employee is the favorite person of at least one other employee, and the only way the company can invite them is if they invite every employee.
The seating arrangement will be the same as that in the figure given in example 1:
- Employee 0 will sit between employees 2 and 1.
- Employee 1 will sit between employees 0 and 2.
- Employee 2 will sit between employees 1 and 0.
The maximum number of employees that can be invited to the meeting is 3.
Example 3:

Input: favorite = [3,0,1,4,1]
Output: 4
Explanation:
The above figure shows how the company will invite employees 0, 1, 3, and 4, and seat them at the round table.
Employee 2 cannot be invited because the two spots next to their favorite employee 1 are taken.
So the company leaves them out of the meeting.
The maximum number of employees that can be invited to the meeting is 4.

Constraints:

n == favorite.length
2 <= n <= 10^5
0 <= favorite[i] <= n - 1
favorite[i] != i
'''


from typing import List


class Solution:
  def maximumInvitations(self, fav: List[int]) -> int:
    n = len(fav)
    edge = [-1] * n
    chain_size = [1] * n
    edges_in = [0] * n
    chain_heads = set([i for i in range(n)])
    count = 1
    dual_nodes_total = 0
    
    for u, v in enumerate(fav):
      edge[u] = v
      edges_in[v] += 1 # 1 edge coming to v
      chain_heads.discard(v)
      
    seen = chain_heads.copy()
    # print('init:', seen)
    
    # find out the longest single-linked-chain's size that 
    # may or may not connect to a cycle
    for head in chain_heads:
      curr = head
      ln = 1
      
      while 0 <= edge[curr] < n:
        # update the current chain size
        seen.add(curr)
        curr = edge[curr]
        ln += 1
        
        # get the longest chain size up to this node
        chain_size[curr] = max(chain_size[curr], ln)
        ln = max(ln, chain_size[curr])
        # print('chain:', head, curr, chain_size[curr])
        
        # there could be another chain comining into this node,
        # or it's a node in a cycle, stop here.
        edges_in[curr] -= 1
        if edges_in[curr] > 0:
          break
        
    # print('chain size:', chain_size, seen, count)
    for i in range(n):
      # the node is in a chain or a cycle that has been
      # visited
      if i in seen:
        continue
        
      cyc_nodes = set()
      curr = i
      
      # loop over and add all nodes in this cycle
      while curr not in cyc_nodes:
        cyc_nodes.add(curr)
        curr = edge[curr]
      
      # a dual-nodes cycle can be tricky -- the 2 nodes in 
      # this cycle can sit next to each other, plus the chains
      # spawning out of these 2 nodes; and all these spawned-dual-cycle
      # can all be put on the same table
      if len(cyc_nodes) == 2:
        a = cyc_nodes.pop()
        b = cyc_nodes.pop()
        dual_nodes_total += chain_size[a] + chain_size[b]
        
      count = max(count, len(cyc_nodes))
      seen |= cyc_nodes
      
    return max(count, dual_nodes_total)
  