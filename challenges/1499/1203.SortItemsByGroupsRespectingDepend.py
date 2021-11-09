'''
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

Example 1:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]

Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.

Constraints:

1 <= m <= n <= 3 * 10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
'''


from typing import List
from collections import defaultdict


class Solution:
  def sortItems0(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
    prior = defaultdict(set)
    dependency = [len(beforeItems[i]) for i in range(n)]
    behind_items = [[] for _ in range(n)]
    groups = defaultdict(set)
    
    for i, g in enumerate(group):
      if g >= 0:
        groups[g].add(i)
        prior[g] |= set(beforeItems[i])
      
      # adding the item to 
      for bi in beforeItems[i]:
        behind_items[bi].append(i)
    
    ans = []
    freed_items = set()
    freed_groups = []
    seen_groups = set([-1])
    
    def add_item(idx: int) -> bool:
      if dependency[idx] > 0:
        return False
      
      for j in behind_items[idx]:
        dependency[j] -= 1
        
        # if the item-j has no more dependencies
        if not dependency[j]:
          freed_items.add(j)
          
        gj = group[j]
        prior[gj].discard(idx)
        
        # if the group the item-j belongs to has no
        # more dependencies
        if not prior[gj] and gj not in seen_groups:
          freed_groups.append(gj)
      
      ans.append(idx)
      freed_items.discard(idx)
      
      return True
    
    def add_group(g: int) -> bool:
      if len(prior[g]) > 0:
        return False
      
      freed = []
      count = 0
      
      for i in groups[g]:
        if i not in freed_items:
          continue
          
        freed_items.discard(i)
        freed.append(i)
        
      while freed:
        i = freed.pop()
        ans.append(i)
        count += 1
        
        for j in behind_items[i]:
          dependency[j] -= 1
          gj = group[j]
          prior[gj].discard(i)

          # if the item-j has no more dependencies
          if not dependency[j]:
            if gj == g:
              freed.append(j)
            else:
              freed_items.add(j)

          # if the group the item-j belongs to has no
          # more dependencies
          if not prior[gj] and gj != g and gj not in seen_groups:
            freed_groups.append(gj)
      
      # print('add group:', g, count, groups[g])
      return count == len(groups[g])
    
    for i in range(n):
      g = group[i]
      
      # discard self-ref for groups
      if i in prior[g] and g >= 0:
        prior[g].discard(i)
        
      # free to use items
      if not beforeItems[i]:
        freed_items.add(i)
        
    for g in prior:
      if not prior[g] and g != -1:
        freed_groups.append(g)
          
    # print(groups, prior, freed_items, freed_groups)
  
    while freed_items or freed_groups:
      # add all freed non-grouped items, quit
      # if illegal case (?)
      freed_none = []
      for i in freed_items:
        if group[i] == -1:
          freed_none.append(i)
          
      for i in freed_none:
        if not add_item(i):
          # print('item q:', i)
          return []
        
      # print('post items', freed_items, freed_groups)
      
      # won't proceed from here anymore
      if not freed_none and not freed_groups:
        break
      
      # add all freed groups, quit if the group
      # has cycles inside the items
      while freed_groups:
        g = freed_groups.pop()
        seen_groups.add(g)
        
        if not add_group(g):
          # print('group q:', g)
          return []
    
    return ans if len(ans) == n else []
  