'''
646. Maximum Length of Pair Chain

You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

Return the length longest chain which can be formed.

You do not need to use up all the given intervals. You can select pairs in any order.

Example 1:

Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
Example 2:

Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:

n == pairs.length
1 <= n <= 1000
-1000 <= lefti < righti <= 1000
'''

from typing import List
from bisect import bisect_left


class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    pairs.sort(key=lambda x: (x[1], x[0]))
    # print(pairs)
    
    end = []
    count = []
    long = 1
    
    for l, r in pairs:
      idx = bisect_left(end, l) - 1
      ln = 1
      
      if 0 <= idx < len(count):
        ln = max(ln, 1+count[idx])
        
      if count:
        ln = max(ln, count[-1])
        
      long = max(long, ln)
      # print((l, r), ln, idx)
      
      if end and r == end[-1]:
        count[-1] = max(count[-1], ln)
      else:
        end.append(r)
        count.append(ln)
        
    # print(end, count)
    
    return long
        