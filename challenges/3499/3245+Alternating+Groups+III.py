'''
3245. Alternating Groups III

There are some red and blue tiles arranged circularly. You are given an array of integers colors and a 2D integers array queries.

The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is a contiguous subset of tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its adjacent tiles in the group).

You have to process queries of two types:

queries[i] = [1, sizei], determine the count of alternating groups with size sizei.
queries[i] = [2, indexi, colori], change colors[indexi] to colori.
Return an array answer containing the results of the queries of the first type in order.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

Example 1:

Input: colors = [0,1,1,0,1], queries = [[2,1,0],[1,4]]

Output: [2]

Explanation:

First query:

Change colors[1] to 0.

Second query:

Count of the alternating groups with size 4:

Example 2:

Input: colors = [0,0,1,0,1,1], queries = [[1,3],[2,3,0],[1,5]]

Output: [2,0]

Explanation:

First query:

Count of the alternating groups with size 3:

Second query: colors will not change.

Third query: There is no alternating group with size 5.

Constraints:

4 <= colors.length <= 5 * 10^4
0 <= colors[i] <= 1
1 <= queries.length <= 5 * 10^4
queries[i][0] == 1 or queries[i][0] == 2
For all i that:
queries[i][0] == 1: queries[i].length == 2, 3 <= queries[i][1] <= colors.length - 1
queries[i][0] == 2: queries[i].length == 3, 0 <= queries[i][1] <= colors.length - 1, 0 <= queries[i][2] <= 1

Test cases:

[0,0,0,1]
[[2,1,1],[1,3],[2,1,1],[2,0,1]]
[0,1,1,0,1]
[[2,1,0],[1,4]]
[0,0,1,0,1,1]
[[1,3],[2,3,0],[1,5]]
[0,1,0,1]
[[1,3],[2,2,1],[1,3],[1,3]]
[1,1,1,0,1]
[[1,4],[2,1,0],[1,3],[1,4]]
[0,1,1,0,1,0]
[[2,5,1],[1,5],[2,3,1],[2,3,1],[1,3]]
[0,1,1,0,1]
[[2,0,1],[1,4],[1,4],[1,3],[2,2,0],[1,3],[2,0,1]]
[1,0,0,1,1]
[[2,2,1],[2,2,1],[2,4,0],[2,2,1],[2,0,0],[1,4],[1,4]]
'''

from typing import List
from collections import defaultdict
from bisect import insort, bisect_right

class Solution:
  '''
  the problem is hard in the sense that there are tons of edge cases to consider and patch;
  
  the core idea is to maintain intervals of all alt-groups, and maintain a counter that can
  calculate the number of intervals with ln >= k; then for interval with ln >= k, its contribution
  to the final counter is `(ln-k+1) * number_of_intervals_with_ln`;

  changing color at a location will possibly lead to the following actions:
  1) move current interval's head to previous interval's tail;
  2) move current interval's tail to next interval's head;
  3) split an interval into 3 intervals (i.e., break from the middle);
  4) if the current interval is a sole element, merge the one before and the one behind;
  '''
  def numberOfAlternatingGroups(self, colors: List[int], queries: List[List[int]]) -> List[int]:
    arr = colors + colors[:-1]
    start = {}
    seg = []
    counter = defaultdict(int)
    i, j = 0, 1
    n = len(colors)
    debug = False
    
    while i < n:
      j = i+1
      while j < len(arr) and arr[j] != arr[j-1]:
        j += 1
      
      seg.append((i, j-1))
      i = j
    
    # combine the rounded
    if seg[-1][1] >= n:
      if seg[-1][0] == 0:
        seg[-1] = (0, n-1)
      else:
        seg = seg[1:]
    
    head = []
    ans = []

    for s, e in seg:
      start[s] = e
      counter[e-s+1] += 1
      head.append(s)
    
    if debug:
      print(seg, head, counter, start)
    
    def count(l0: int) -> int:
      if len(head) == 1:
        if l0 > n:
          return 0
        
        h0 = head[0]
        t0 = start[h0]
        
        if colors[h0%n] != colors[t0%n]:
          # circular
          return n

      c = 0
      for l1, cnt in counter.items():
        if l1 < l0:
          continue
          
        c += (l1-l0+1) * cnt
        
      return c
    
    def partition(p0, idx):
      h = head[p0]
      t = start[h]
      m = len(head)
      l0 = t-h+1
      
      # remove and merge
      if l0 == 1 and colors[idx%n] != colors[(idx+1)%n] and colors[idx%n] != colors[(idx-1+n)%n] and m > 2:
        # remove self
        del start[h]
        counter[1] -= 1
        
        pl = (m+p0-1) % m
        hl = head[pl]
        tl = start[hl]
        ll = tl-hl+1
        
        pr = (p0+1) % m
        hr = head[pr]
        tr = start[hr]
        lr = tr-hr+1
        
        head.remove(h)
        head.remove(hr)
        start[hl] = tr + (n if tr < hl else 0)
        del start[hr]
        
        counter[ll] -= 1
        if not counter[ll]:
          del counter[ll]
        
        counter[lr] -= 1
        if not counter[lr]:
          del counter[lr]
          
        counter[ll+lr+1] += 1
        
        return
        
      if h == idx:
        # is the group head
        if len(head) == 1:
          # sole group, head to tail
          if colors[t%n] != colors[idx%n]:
            h0 = (h+1) % n
            t = (h0-1+n)
            
            del start[h]
            start[h0] = t
            head[0] = h0
              
            return
          
          # sole group, split
          counter[l0] -= 1
          if not counter[l0]:
            del counter[l0]
          
          counter[l0-1] += 1
          counter[1] += 1
          
          start[h] = h
          h0 = h+1
          
          if h0 >= n:
            start[h0-n] = t-n
            insort(head, h0-n)
          else:
            start[h0] = t
            insort(head, h0)
          
        else:
          p1 = (m+p0-1) % m
          h1 = head[p1]
          t1 = start[h1]
          l1 = t1-h1+1
          
          counter[l0] -= 1
          if not counter[l0]:
            del counter[l0]
            
          counter[l1] -= 1
          if not counter[l1]:
            del counter[l1]
            
          counter[l1+1] += 1
          start[h1] += 1
          
          head.remove(h)
          del start[h]
          
          if l0 > 1:          
            counter[l0-1] += 1
            h0 = h+1
            
            if h0 >= n:
              start[h0-n] = t-n
              insort(head, h0-n)
            else:
              start[h0] = t
              insort(head, h0)

      elif t == idx:
        # is the group tail
        if len(head) == 1:
          # sole group, tail to head
          if colors[h%n] != colors[idx%n]:
            h0 = (h-1+n) % n
            t = (h0-1+n)
            
            del start[h]
            start[h0] = t
            head[0] = h0
              
            return
          
          # sole group, split
          counter[l0] -= 1
          counter[l0-1] += 1
          counter[1] += 1
          
          start[h] = t-1
          h0 = t
          
          if h0 >= n:
            start[h0-n] = h0-n
            insort(head, h0-n)
          else:
            start[h0] = h0
            insort(head, h0)
          
        else:
          p1 = (p0+1) % m
          h1 = head[p1]
          t1 = start[h1]
          l1 = t1-h1+1
          
          counter[l0] -= 1
          if not counter[l0]:
            del counter[l0]
          
          counter[l1] -= 1
          if not counter[l1]:
            del counter[l1]
          
          if l0 > 1:
            counter[l0-1] += 1
          
          counter[l1+1] += 1
          
          head.remove(h1)
          del start[h1]
          
          h1 -= 1
          if h1 < 0:
            h1 += n
            t1 += n
            start[h1] = t1
            insort(head, h1)
            
          else:
            start[h1] = t1
            insort(head, h1)
          
          if l0 == 1:
            del start[h]
          else:
            start[h] -= 1

      else:
        # break a circular
        if len(head) == 1 and colors[h%n] != colors[t%n]:
          counter[l0] -= 1
          counter[l0-1] += 1
          counter[1] += 1
          
          h0 = idx+1
          if h0 >= n:
            h0 -= n
            t0 = idx-1
          else:
            t0 = idx-1+n
            
          head.remove(h)
          insort(head, idx)
          insort(head, h0)
          
          del start[h]
          start[h0] = t0
          start[idx] = idx
          
          return
          
        # is in the middle, split
        l00 = l0 - (t-idx+1)
        counter[l0] -= 1
        counter[l00] += 1
        counter[1] += 1
        counter[t-idx] += 1
        
        start[h] = idx-1
        
        h1 = idx+1
        if h1 >= n:
          h1 -= n
          t -= n
          
        if idx >= n:
          idx -= n
          
        start[idx] = idx
        insort(head, idx)
          
        start[h1] = t
        insort(head, h1)
    
    def update(idx: int, c: int):
      # no changes
      if c == colors[idx]:
        return
      
      colors[idx] = c
      
      if idx < head[0]:
        # in the last group
        partition(len(head)-1, idx+n)
        
      else:
        # in a front group, find the group head
        p0 = bisect_right(head, idx)-1
        partition(p0, idx)
      
    for q in queries:
      if q[0] == 1:
        # get group counts
        ans.append(count(q[1]))
      else:
        # update segments
        update(q[1], q[2])  
    
      if debug:
        print('q:', q, head, counter, start)
      
    return ans
        