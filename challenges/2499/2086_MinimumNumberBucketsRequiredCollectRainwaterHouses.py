'''
You are given a 0-indexed string street. Each character in street is either 'H' representing a house or '.' representing an empty space.

You can place buckets on the empty spaces to collect rainwater that falls from the adjacent houses. The rainwater from a house at index i is collected if a bucket is placed at index i - 1 and/or index i + 1. A single bucket, if placed adjacent to two houses, can collect the rainwater from both houses.

Return the minimum number of buckets needed so that for every house, there is at least one bucket collecting rainwater from it, or -1 if it is impossible.

Example 1:

Input: street = "H..H"
Output: 2
Explanation:
We can put buckets at index 1 and index 2.
"H..H" -> "HBBH" ('B' denotes where a bucket is placed).
The house at index 0 has a bucket to its right, and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
Example 2:

Input: street = ".H.H."
Output: 1
Explanation:
We can put a bucket at index 2.
".H.H." -> ".HBH." ('B' denotes where a bucket is placed).
The house at index 1 has a bucket to its right, and the house at index 3 has a bucket to its left.
Thus, for every house, there is at least one bucket collecting rainwater from it.
Example 3:

Input: street = ".HHH."
Output: -1
Explanation:
There is no empty space to place a bucket to collect the rainwater from the house at index 2.
Thus, it is impossible to collect the rainwater from all the houses.

Constraints:

1 <= street.length <= 10^5
street[i] is either'H' or '.'.
'''

from heapq import heappush, heappop


class Solution:
  def minimumBuckets(self, street: str) -> int:
    h = set()
    s = []
    n = len(street)
    if n == 1:
      return 0 if street[0] == '.' else -1
    
    for i, ch in enumerate(street):
      if ch == 'H':
        h.add(i)
        if (i-1 in h) and (i == n-1 or street[i+1] == 'H' or i-1 == 0):
          # print('??0')
          return -1
        
      else:
        if i == 0 or i == n-1:
          cnt = 1 if ((i == 0 and street[1] == 'H') or (i == n-1 and street[i-1] == 'H')) else 0
        else:
          cnt = (1 if street[i-1] == 'H' else 0) + (1 if street[i+1] == 'H' else 0)
          
        # print(i, cnt)
        if cnt > 0:
          heappush(s, (-cnt, i))
          
    count = 0
    # print(s)
    
    if not s:
      # print('??1', s)
      return 0 if len(h) == 0 else -1
    
    while h and s:
      c, i = heappop(s)
      nc = (-1 if i-1 in h else 0) + (-1 if i+1 in h else 0)
      if nc == 0:
        continue
        
      if nc != c:
        heappush(s, (nc, i))
        continue
        
      count += 1
      # print(i)
      
      h.discard(i-1)
      h.discard(i+1)
      
    return count
    